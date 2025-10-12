# Python CDMX - Terraform Infrastructure

Este directorio contiene la infraestructura como código (IaC) para el sitio web de Python CDMX usando AWS.

## 📋 Arquitectura

```
                    ┌──────────────────────┐
                    │   Route53 Hosted     │
                    │   pythoncdmx.org     │
                    └──────────┬───────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
    ┌───────────▼──────────┐     ┌───────────▼──────────┐
    │  pythoncdmx.org      │     │ staging.pythoncdmx.org│
    │  www.pythoncdmx.org  │     │   (Testing)           │
    └───────────┬──────────┘     └───────────┬───────────┘
                │                            │
                │ HTTPS (TLS 1.2+)          │ HTTPS (TLS 1.2+)
                │                            │
                ▼                            ▼
    ┌─────────────────────┐    ┌─────────────────────┐
    │ CloudFront PROD     │    │ CloudFront STAGING  │
    │ - ACM Certificate   │    │ - ACM Certificate   │
    │ - Cache: 1h-24h     │    │ - Cache: 5min-2h    │
    │ - Gzip/Brotli       │    │ - Shorter TTL       │
    └──────────┬──────────┘    └──────────┬──────────┘
               │                           │
               │ OAC (SigV4)              │ OAC (SigV4)
               │                           │
               ▼                           ▼
    ┌──────────────────────┐  ┌──────────────────────┐
    │ S3: pythoncdmx-      │  │ S3: pythoncdmx-      │
    │     website (PROD)   │  │     website-staging  │
    │ - Private            │  │ - Private            │
    │ - Versioning         │  │ - Versioning         │
    │ - AES256             │  │ - AES256             │
    └──────────────────────┘  └──────────────────────┘
```

## 🚀 Recursos Creados

### 🌐 Route53 (DNS)
- **Hosted Zone**: pythoncdmx.org (existente, solo se agregan registros)
- **Registros Production**:
  - A/AAAA: `pythoncdmx.org` → CloudFront PROD
  - A/AAAA: `www.pythoncdmx.org` → CloudFront PROD
- **Registros Staging**:
  - A/AAAA: `staging.pythoncdmx.org` → CloudFront STAGING
- **Validación ACM**: Registros CNAME automáticos para certificados

### 📦 Production Environment

#### 1. **S3 Bucket (Production)**
- **Nombre**: `pythoncdmx-website`
- **Acceso**: Privado (solo CloudFront puede acceder)
- **Características**:
  - ✅ Versioning habilitado
  - ✅ Encriptación AES256
  - ✅ Lifecycle: 90 días versiones antiguas
  - ✅ CORS configurado

#### 2. **CloudFront Distribution (Production)**
- **Dominios**: pythoncdmx.org, www.pythoncdmx.org
- **Características**:
  - ✅ Certificado SSL/TLS (ACM)
  - ✅ HTTP/2 y HTTP/3 habilitado
  - ✅ Compresión Gzip/Brotli
  - ✅ Cache optimizado (HTML: 10min, Assets: 24h, Images: 7d)
  - ✅ IPv6 habilitado
  - ✅ Origin Access Control (OAC)

#### 3. **ACM Certificate (Production)**
- **Región**: us-east-1 (requerido para CloudFront)
- **Validación**: DNS automática vía Route53
- **Dominios cubiertos**:
  - pythoncdmx.org
  - www.pythoncdmx.org

### 🧪 Staging Environment

#### 4. **S3 Bucket (Staging)**
- **Nombre**: `pythoncdmx-website-staging`
- **Acceso**: Privado (solo CloudFront puede acceder)
- **Características**:
  - ✅ Versioning habilitado
  - ✅ Encriptación AES256
  - ✅ Lifecycle: 30 días versiones antiguas (más agresivo)
  - ✅ CORS configurado

#### 5. **CloudFront Distribution (Staging)**
- **Dominio**: staging.pythoncdmx.org
- **Características**:
  - ✅ Certificado SSL/TLS (ACM)
  - ✅ Cache más corto (HTML: 1min, Assets: 30min, Images: 1h)
  - ✅ IPv6 habilitado
  - ✅ Banner "STAGING" en todas las páginas

#### 6. **ACM Certificate (Staging)**
- **Región**: us-east-1
- **Validación**: DNS automática vía Route53
- **Dominio**: staging.pythoncdmx.org

### 🔒 Security & State

#### 7. **IAM Role (GitHub Actions)**
- **OIDC Provider**: GitHub Actions sin credenciales long-lived
- **Permisos**:
  - S3: Read/Write en ambos buckets (prod y staging)
  - CloudFront: Invalidación de cache en ambas distribuciones
  - Scope: Repositorio PythonMexico/pythonCDMX

#### 8. **Backend State**
- **S3 Bucket**: `pythoncdmx-terraform-state`
- **DynamoDB**: `pythoncdmx-terraform-locks`
- **Encriptación**: Habilitada

## 📦 Prerequisitos

1. **Terraform** >= 1.0
   ```bash
   brew install terraform  # macOS
   ```

2. **AWS CLI** configurado
   ```bash
   aws configure
   ```

3. **Route53 Hosted Zone** ya creada para `pythoncdmx.org`
   ```bash
   # Verificar hosted zone existente
   aws route53 list-hosted-zones
   ```

4. **Permisos AWS requeridos**:
   - S3: Crear/modificar buckets
   - CloudFront: Crear/modificar distribuciones
   - ACM: Solicitar/validar certificados
   - Route53: Crear/modificar registros DNS
   - IAM: Crear roles y políticas

## 🔧 Configuración Inicial

### 1. Crear Backend de Terraform (Una sola vez)

```bash
# Crear bucket para Terraform state
aws s3 mb s3://pythoncdmx-terraform-state --region us-east-1

# Habilitar versioning
aws s3api put-bucket-versioning \
  --bucket pythoncdmx-terraform-state \
  --versioning-configuration Status=Enabled

# Habilitar encriptación
aws s3api put-bucket-encryption \
  --bucket pythoncdmx-terraform-state \
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "AES256"
      }
    }]
  }'

# Crear tabla DynamoDB para locks
aws dynamodb create-table \
  --table-name pythoncdmx-terraform-locks \
  --attribute-definitions AttributeName=LockID,AttributeType=S \
  --key-schema AttributeName=LockID,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --region us-east-1
```

### 2. Validar Dominio en ACM

**✅ AUTOMÁTICO**: La validación DNS se hace automáticamente vía Route53. Terraform crea los registros CNAME necesarios y espera la validación.

Si necesitas verificar el estado:

```bash
# Ver certificados y su estado
aws acm list-certificates --region us-east-1

# Ver detalles de validación
terraform output certificate_validation_records
```

**Tiempo de validación**: 5-30 minutos (automático)

## 🏗️ Despliegue

### Inicializar Terraform

```bash
cd terraform
terraform init
```

### Plan de Cambios

```bash
terraform plan
```

### Aplicar Infraestructura

```bash
terraform apply
```

Terraform creará:
- ✅ 2 S3 buckets privados (production + staging)
- ✅ 2 CloudFront distributions
- ✅ 2 Certificados ACM (validación DNS automática)
- ✅ Registros DNS en Route53
- ✅ IAM Role con OIDC para GitHub Actions
- ✅ Políticas de acceso
- ✅ Cache behaviors optimizados

**⏱️ Tiempo estimado**: 15-30 minutos (mayoría es validación de certificados)

### Obtener Outputs

```bash
terraform output
```

Outputs importantes:
- **Production**:
  - `website_url`: https://pythoncdmx.org
  - `cloudfront_distribution_id`: ID para invalidación de cache
  - `website_bucket_name`: pythoncdmx-website
- **Staging**:
  - `staging_website_url`: https://staging.pythoncdmx.org
  - `staging_cloudfront_distribution_id`: ID para invalidación de cache staging
  - `staging_bucket_name`: pythoncdmx-website-staging
- **Route53**:
  - `hosted_zone_id`: ID de la hosted zone
  - `hosted_zone_name_servers`: Name servers (para verificación)

## 🔐 Configuración de GitHub Actions

El deploy automático requiere configurar secretos en GitHub:

### 1. Crear IAM Role para GitHub OIDC

```bash
# Ver terraform/iam-github.tf (crear este archivo)
terraform apply
```

### 2. Configurar Secrets en GitHub

En el repositorio, ir a **Settings > Secrets and variables > Actions**:

```bash
# Obtener valores de Terraform
terraform output

# Configurar estos secrets:
AWS_ROLE_ARN: arn:aws:iam::123456789012:role/GitHubActionsDeployRole
CLOUDFRONT_DISTRIBUTION_ID: E1234ABCDEF567 (production)
CLOUDFRONT_DISTRIBUTION_ID_STAGING: E7890GHIJKL123 (staging)
```

### 3. Workflows Configurados

**Production** (`.github/workflows/deploy-aws.yml`):
- **Trigger**: Push a `main`
- **Destino**: pythoncdmx.org
- **S3 Bucket**: pythoncdmx-website
- **Cache**: Agresivo (1h-24h)

**Staging** (`.github/workflows/deploy-staging.yml`):
- **Trigger**: Push a `develop`/`staging` o PR a `main`
- **Destino**: staging.pythoncdmx.org
- **S3 Bucket**: pythoncdmx-website-staging
- **Cache**: Corto (1min-2h)
- **Banner**: "🚧 STAGING ENVIRONMENT" en todas las páginas

## 📊 Gestión de Cache

### Invalidar Cache Completo

```bash
aws cloudfront create-invalidation \
  --distribution-id E1234ABCDEF567 \
  --paths "/*"
```

### Invalidar Paths Específicos

```bash
aws cloudfront create-invalidation \
  --distribution-id E1234ABCDEF567 \
  --paths "/index.html" "/css/*"
```

### Verificar Estado de Invalidación

```bash
aws cloudfront get-invalidation \
  --distribution-id E1234ABCDEF567 \
  --id I1234ABCDEF567
```

## 🔄 Estrategia de Cache

### HTML Files
- Cache: 10 minutos
- Header: `Cache-Control: public, max-age=600, must-revalidate`

### Assets Estáticos (CSS/JS)
- Cache: 24 horas
- Header: `Cache-Control: public, max-age=86400`

### Imágenes
- Cache: 7 días
- Header: `Cache-Control: public, max-age=604800`

### Sitemap
- Cache: Sin cache
- Header: `Cache-Control: public, max-age=0, must-revalidate`

## 💰 Costos Estimados

### Free Tier (Primer Año)
- S3: 5GB de almacenamiento
- CloudFront: 50GB de transferencia
- ACM: Certificados gratuitos

### Después de Free Tier (Estimado Mensual)
- S3: ~$0.50 (20GB)
- CloudFront: ~$2-5 (dependiendo del tráfico)
- **Total**: ~$3-6/mes

## 🔍 Troubleshooting

### Error: Certificate validation timeout

**Problema**: El certificado ACM no se valida automáticamente.

**Solución**:
1. Verifica que Route53 tenga los registros de validación:
   ```bash
   aws route53 list-resource-record-sets --hosted-zone-id ZXXXXX
   ```
2. Los registros deben ser tipo CNAME con nombres `_abc123.pythoncdmx.org`
3. Terraform crea estos automáticamente, pero puede tardar 5-30 minutos
4. Si persiste el error después de 45 minutos, revisar permisos de Route53

### Error: S3 bucket already exists

**Problema**: El nombre del bucket ya está en uso.

**Solución**:
```bash
# Cambiar nombre en variables.tf
bucket_name = "pythoncdmx-website-prod"
```

### Error: Access Denied al subir a S3

**Problema**: Permisos insuficientes del IAM role.

**Solución**:
1. Verificar políticas del role: `terraform/iam-github.tf`
2. Confirmar trust relationship con GitHub OIDC
3. Revisar logs de CloudWatch

### CloudFront muestra contenido antiguo

**Problema**: Cache no invalidado.

**Solución**:
```bash
aws cloudfront create-invalidation \
  --distribution-id $DISTRIBUTION_ID \
  --paths "/*"
```

## 🔒 Seguridad

### Buenas Prácticas Implementadas

✅ **S3 Bucket privado**: No acceso público directo
✅ **Origin Access Control**: CloudFront usa firma SigV4
✅ **Encriptación en reposo**: AES256 en S3
✅ **TLS 1.2+**: Protocolo mínimo seguro
✅ **Versioning**: Protección contra eliminación accidental
✅ **IAM Roles**: Sin credenciales hardcoded
✅ **OIDC GitHub**: Autenticación sin long-lived tokens

### Checklist de Seguridad

- [ ] Backend state encriptado
- [ ] S3 bucket policy restrictiva
- [ ] CloudFront usa HTTPS únicamente
- [ ] Certificado SSL válido
- [ ] IAM roles con least privilege
- [ ] Logs de acceso habilitados (opcional)
- [ ] AWS WAF configurado (opcional para producción)

## 🛠️ Mantenimiento

### Actualizar Infraestructura

```bash
cd terraform
terraform plan
terraform apply
```

### Backup de State

```bash
# Descargar state actual
aws s3 cp s3://pythoncdmx-terraform-state/website/terraform.tfstate ./backup-$(date +%Y%m%d).tfstate
```

### Destruir Infraestructura (PELIGRO)

```bash
# ⚠️ Esto eliminará TODOS los recursos
terraform destroy
```

## 🌍 Gestión de Entornos

### Diferencias Production vs Staging

| Aspecto | Production | Staging |
|---------|-----------|---------|
| **Dominio** | pythoncdmx.org | staging.pythoncdmx.org |
| **S3 Bucket** | pythoncdmx-website | pythoncdmx-website-staging |
| **Cache HTML** | 10 minutos | 1 minuto |
| **Cache Assets** | 24 horas | 30 minutos |
| **Cache Images** | 7 días | 1 hora |
| **Lifecycle S3** | 90 días | 30 días |
| **Deploy Trigger** | Push a `main` | Push a `develop`/staging |
| **Banner** | No | Sí ("STAGING ENV") |

### Flujo de Trabajo Recomendado

1. **Desarrollo**: Crear branch de feature
2. **Testing**: Merge a `develop` → Deploy a staging
3. **QA**: Probar en https://staging.pythoncdmx.org
4. **Producción**: PR a `main` → Review → Merge → Deploy automático

## 📚 Referencias

- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [CloudFront con S3](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.SimpleDistribution.html)
- [ACM Certificate Validation](https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html)
- [Route53 Records](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html)
- [GitHub OIDC con AWS](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services)

## 📞 Soporte

Para problemas con la infraestructura:
1. Revisar esta documentación
2. Consultar logs de CloudWatch
3. Verificar estado de recursos: `terraform show`
4. Abrir issue en el repositorio
5. Contactar al equipo de infraestructura

---

**Última actualización**: 2025-01-11
**Mantenido por**: Equipo Python CDMX
**Versión**: 2.0 (Route53 + Staging Environment)
