# Fix para URLs sin extensión .html en producción

## Problema
Los enlaces funcionaban correctamente en local pero no en producción. Por ejemplo:
- ❌ `https://pythoncdmx.org/meetups/` no funcionaba
- ✅ `https://pythoncdmx.org/meetups/index.html` sí funcionaba

## Causa
El problema se debía a que CloudFront no estaba configurado para manejar URLs sin extensión `.html`. Cuando MkDocs genera el sitio con `use_directory_urls: true`, crea URLs como `/meetups/` que apuntan a `/meetups/index.html`, pero CloudFront no sabía cómo resolver estas URLs.

## Solución Implementada

### 1. Configuración en mkdocs.yml
```yaml
# URL configuration
use_directory_urls: true
```

### 2. CloudFront Function
Se agregó una función CloudFront que maneja automáticamente las URLs sin extensión:

```javascript
function handler(event) {
    var request = event.request;
    var uri = request.uri;

    // If the URI ends with a slash, try to serve index.html
    if (uri.endsWith('/')) {
        request.uri = uri + 'index.html';
    }
    // If the URI doesn't have an extension, try to add .html
    else if (!uri.includes('.') && !uri.endsWith('/')) {
        request.uri = uri + '.html';
    }

    return request;
}
```

### 3. Asociación con Cache Behaviors
La función se asoció con todos los cache behaviors de CloudFront para asegurar consistencia.

## Archivos Modificados

1. **mkdocs.yml**: Agregada configuración `use_directory_urls: true`
2. **terraform/cloudfront.tf**: 
   - Agregada CloudFront Function `url_rewrite`
   - Asociada la función con todos los cache behaviors
3. **terraform/cloudfront-staging.tf**:
   - Aplicada la misma CloudFront Function a staging
   - Asociada la función con todos los cache behaviors de staging

## Despliegue

Para aplicar estos cambios:

1. **Aplicar cambios de Terraform**:
   ```bash
   cd terraform
   terraform plan
   terraform apply
   ```

2. **Desplegar el sitio**:
   ```bash
   # Los cambios se aplicarán automáticamente en el próximo deploy
   git push origin main
   ```

## Verificación

Después del despliegue, verificar que funcionen:

### Producción
- ✅ `https://pythoncdmx.org/meetups/`
- ✅ `https://pythoncdmx.org/meetups/index.html`
- ✅ `https://pythoncdmx.org/about/`
- ✅ `https://pythoncdmx.org/about/index.html`

### Staging
- ✅ `https://staging.pythoncdmx.org/meetups/`
- ✅ `https://staging.pythoncdmx.org/meetups/index.html`
- ✅ `https://staging.pythoncdmx.org/about/`
- ✅ `https://staging.pythoncdmx.org/about/index.html`

## Notas Técnicas

- La CloudFront Function se ejecuta en el edge, por lo que tiene latencia mínima
- La función solo modifica la URI si es necesario, sin afectar assets estáticos
- Los cache behaviors mantienen sus configuraciones originales de TTL
- La solución es compatible con el comportamiento existente de MkDocs

## Referencias

- [MkDocs use_directory_urls documentation](https://www.mkdocs.org/user-guide/configuration/#use_directory_urls)
- [CloudFront Functions documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html)
