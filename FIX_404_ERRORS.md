# Solución a Errores 404 en pythoncdmx.org

## 📋 Resumen del Problema

**Problema identificado:** Las URLs de subdirectorios (`/meetups/`, `/comunidad/`, etc.) devuelven error 404, mientras que la página principal funciona correctamente.

**Causa raíz:**
- MkDocs genera el sitio con `--use-directory-urls`, creando URLs limpias como `/meetups/` → `site/meetups/index.html`
- CloudFront tiene configurado `default_root_object = "index.html"` que **solo funciona para la raíz** (`/`)
- Para subdirectorios, CloudFront busca un objeto llamado `meetups/` en S3 (sin `index.html`)
- Como ese objeto no existe, S3 devuelve 403, que CloudFront convierte en 404

## ✅ Solución Implementada

Se implementó **CloudFront Functions** para reescribir automáticamente las URLs y agregar `index.html` a las rutas que terminan en `/` o no tienen extensión.

### Archivos Modificados/Creados

#### 1. **Nuevo:** `terraform/cloudfront-function.tf`
- Crea dos CloudFront Functions (producción y staging)
- Función JavaScript que intercepta requests y añade `index.html` automáticamente
- Maneja dos casos:
  - URLs que terminan en `/` → Añade `index.html`
  - URLs sin extensión de archivo → Añade `/index.html`

#### 2. **Modificado:** `terraform/cloudfront.tf`
- Líneas 46-50: Asocia la función CloudFront al `default_cache_behavior`
- La función se ejecuta en el evento `viewer-request` (antes de llegar a S3)

#### 3. **Modificado:** `terraform/cloudfront-staging.tf`
- Líneas 46-50: Asocia la función CloudFront de staging al `default_cache_behavior`
- Misma lógica aplicada al ambiente de staging

## 🚀 Pasos para Desplegar

### Prerequisitos
- Acceso a AWS con credenciales configuradas
- Terraform instalado
- Variables de Terraform configuradas (archivo `terraform.tfvars`)

### Despliegue

1. **Navega al directorio de Terraform:**
   ```bash
   cd terraform
   ```

2. **Revisa el plan de Terraform:**
   ```bash
   terraform plan
   ```

   Deberías ver:
   - `+ aws_cloudfront_function.directory_index` (nuevo)
   - `+ aws_cloudfront_function.directory_index_staging` (nuevo)
   - `~ aws_cloudfront_distribution.website` (modificado)
   - `~ aws_cloudfront_distribution.website_staging` (modificado)

3. **Aplica los cambios:**
   ```bash
   terraform apply
   ```

4. **Confirma los cambios:** Escribe `yes` cuando se te solicite

### Tiempo de Propagación

- **CloudFront Functions:** Se despliegan inmediatamente en todas las edge locations
- **Distribución de CloudFront:** Puede tardar 5-15 minutos en propagarse completamente
- **Cache:** Si hay contenido en caché, puede tardar hasta 1 hora (basado en `max_ttl`)

### Invalidación de Caché (Opcional pero Recomendado)

Para aplicar los cambios inmediatamente sin esperar la expiración del caché:

```bash
# Para producción
aws cloudfront create-invalidation \
  --distribution-id <DISTRIBUTION_ID> \
  --paths "/*"

# Para staging
aws cloudfront create-invalidation \
  --distribution-id <STAGING_DISTRIBUTION_ID> \
  --paths "/*"
```

Puedes obtener los Distribution IDs con:
```bash
terraform output cloudfront_distribution_id
terraform output cloudfront_staging_distribution_id
```

## 🧪 Verificación

Una vez desplegado, verifica que las siguientes URLs funcionan:

### Producción (pythoncdmx.org)
- ✅ `https://pythoncdmx.org/` (ya funcionaba)
- ✅ `https://pythoncdmx.org/meetups/`
- ✅ `https://pythoncdmx.org/meetups/2025/`
- ✅ `https://pythoncdmx.org/comunidad/`
- ✅ `https://pythoncdmx.org/comunidad/ponentes/`
- ✅ `https://pythoncdmx.org/comunidad/voluntarios/`
- ✅ `https://pythoncdmx.org/blog/`

### Staging (si aplica)
- ✅ Todas las rutas equivalentes en el dominio de staging

## 📊 Impacto y Beneficios

### Ventajas de la Solución
- ✅ **URLs limpias:** Mantiene `/meetups/` en lugar de `/meetups.html`
- ✅ **SEO amigable:** Las URLs siguen siendo las mismas
- ✅ **Sin cambios en el código:** No requiere modificar MkDocs
- ✅ **Bajo costo:** CloudFront Functions es prácticamente gratis ($0.10 por millón de invocaciones)
- ✅ **Alta performance:** Se ejecuta en edge locations (latencia mínima)
- ✅ **Escalable:** Funciona automáticamente para cualquier nueva página

### Costo Estimado
- **CloudFront Functions:** ~$0.10 por millón de requests
- Para un sitio con 100,000 visitas/mes: **~$0.01/mes**

## 🔍 Debugging

Si después del despliegue aún hay errores 404:

1. **Verifica que la función esté asociada:**
   ```bash
   aws cloudfront get-distribution --id <DISTRIBUTION_ID> \
     | jq '.Distribution.DistributionConfig.DefaultCacheBehavior.FunctionAssociations'
   ```

2. **Verifica que la función esté publicada:**
   ```bash
   aws cloudfront list-functions
   ```

3. **Revisa CloudWatch Logs (si está habilitado):**
   ```bash
   aws logs tail /aws/cloudfront/function/pythoncdmx-directory-index --follow
   ```

4. **Invalida el caché de CloudFront** (ver comando arriba)

5. **Prueba con curl para ver headers:**
   ```bash
   curl -I https://pythoncdmx.org/meetups/
   ```

## 📝 Notas Técnicas

### Cómo Funciona la CloudFront Function

```javascript
function handler(event) {
    var request = event.request;
    var uri = request.uri;

    // Ejemplo: /meetups/ → /meetups/index.html
    if (uri.endsWith('/')) {
        request.uri += 'index.html';
    }
    // Ejemplo: /meetups → /meetups/index.html
    else if (!uri.includes('.')) {
        request.uri += '/index.html';
    }

    return request;
}
```

**Flujo de ejecución:**
1. Usuario solicita `https://pythoncdmx.org/meetups/`
2. CloudFront recibe el request en la edge location
3. **CloudFront Function** intercepta y reescribe: `/meetups/` → `/meetups/index.html`
4. CloudFront solicita a S3: `s3://bucket/meetups/index.html`
5. S3 devuelve el archivo (existe en S3 gracias a MkDocs)
6. CloudFront devuelve la respuesta al usuario

### Alternativas Consideradas (No Implementadas)

1. **Lambda@Edge:** Más potente pero:
   - ❌ Más costoso (~$0.60 por millón vs $0.10)
   - ❌ Mayor latencia (ejecuta en regional edge cache)
   - ❌ Más complejo de mantener

2. **Cambiar a `--no-directory-urls`:**
   - ❌ URLs menos amigables (`/meetups.html`)
   - ❌ Rompe links existentes
   - ❌ Peor SEO

3. **S3 Redirects:**
   - ❌ No funciona con CloudFront OAC
   - ❌ Requiere S3 public (inseguro)

## 🎯 Próximos Pasos

1. **Desplegar los cambios** siguiendo la sección "Pasos para Desplegar"
2. **Verificar** que todas las URLs funcionan correctamente
3. **Monitorear** CloudFront metrics durante las primeras 24 horas
4. **Documentar** en el README del proyecto que se usa CloudFront Functions

## 🆘 Soporte

Si encuentras problemas durante el despliegue:

1. Revisa el output de `terraform plan` y `terraform apply`
2. Verifica los logs de CloudWatch (si están habilitados)
3. Consulta la documentación de AWS:
   - [CloudFront Functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html)
   - [CloudFront Distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-working-with.html)

---

**Fecha de implementación:** 2025-10-25
**Autor:** Claude Code
**Versión:** 1.0
