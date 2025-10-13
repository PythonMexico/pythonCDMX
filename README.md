# Python CDMX - Sitio Web de la Comunidad

> *"Vine por el código, me quedé por la comunidad"*

Sitio web oficial de la comunidad Python CDMX, construido con **MkDocs Material** y diseño **Material Design** optimizado. Documentamos todos nuestros meetups, charlas y eventos, conectando a la comunidad Python de la Ciudad de México.

[![Deploy AWS Production](https://github.com/PythonMexico/pythonCDMX/actions/workflows/deploy-aws.yml/badge.svg)](https://github.com/PythonMexico/pythonCDMX/actions/workflows/deploy-aws.yml)
[![Deploy Staging](https://github.com/PythonMexico/pythonCDMX/actions/workflows/deploy-staging.yml/badge.svg)](https://github.com/PythonMexico/pythonCDMX/actions/workflows/deploy-staging.yml)
[![Sitio Web](https://img.shields.io/badge/sitio-pythoncdmx.org-4CAF50)](https://pythoncdmx.org)

## Características Principales

- **Material Design moderno** - Interfaz limpia con modo claro/oscuro automático
- **Completamente responsive** - Optimizado para móvil, tablet y escritorio
- **Búsqueda avanzada** - Encuentra charlas por tema, ponente o contenido
- **Videos integrados** - Acceso directo a nuestras charlas en YouTube
- **CSS optimizado** - Sistema de 18+ variables centralizadas, arquitectura variables-first
- **Enlaces de comunidad** - Botones con colores oficiales de cada plataforma
- **Estadísticas de comunidad** - Métricas y datos de participación
- **Despliegue automático** - CI/CD con GitHub Actions

## Inicio Rápido

### Prerrequisitos

- **Python 3.8+**
- **pip** o **pipenv**

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/PythonMexico/pythonCDMX.git
cd pythonCDMX

# Instalar dependencias
pip install -r requirements.txt
```

### Desarrollo Local

```bash
# Servidor de desarrollo con recarga automática
mkdocs serve

# El sitio estará disponible en:
# http://localhost:8000
```

### Construcción para Producción

```bash
# Generar sitio estático
mkdocs build

# Los archivos se generan en la carpeta site/
```

## Estructura del Proyecto

```
python-cdmx-charlas/
├── docs/                          # Contenido principal
│   ├── css/
│   │   └── custom.css            # Estilos optimizados (~1466 líneas, variables-first)
│   ├── components/               # Componentes reutilizables
│   │   ├── community-links.md    # Enlaces de redes sociales
│   │   └── quick-navigation.md   # Navegación de páginas
│   ├── images/                   # Assets e imágenes
│   ├── meetups/                  # Eventos por año
│   │   ├── 2023/
│   │   ├── 2024/
│   │   └── 2025/
│   ├── comunidad/                # Páginas de comunidad
│   │   ├── ponentes.md
│   │   ├── voluntarios.md
│   │   └── alianzas.md
│   └── index.md                  # Página principal
├── scripts/                      # Herramientas de automatización
│   ├── generate_meetups.py       # Generador de páginas
│   ├── check_links.py           # Verificador de enlaces
│   └── metadata_json/           # Datos de meetups
├── .github/workflows/           # CI/CD con GitHub Actions
├── mkdocs.yml                   # Configuración de MkDocs
├── requirements.txt             # Dependencias Python
└── README.md                    # Este archivo
```

## Sistema de Diseño

### Colores Principales
- **Verde Python**: `#4CAF50` (color primario)
- **Verde Oscuro**: `#45a049` (hover states)
- **Modo automático**: Claro/oscuro según preferencia del sistema

### Componentes CSS
- **Variables centralizadas** - 18+ variables CSS para colores, badges, transiciones y espaciado
- **Arquitectura variables-first** - Zero colores hardcoded, mantenibilidad máxima
- **Sistema de botones** - `.btn-primary`, `.btn`, `.btn-nav` con variables unificadas
- **Sistema de badges** - 8 tipos de roles con colores centralizados
- **Tarjetas unificadas** - `.volunteer-card` para ponentes y voluntarios
- **Enlaces de comunidad** - Colores oficiales por plataforma usando variables
- **Responsive design** - Breakpoint único en 768px, mobile-first approach
- **Zero `!important`** - Arquitectura CSS limpia con especificidad apropiada

## Documentación

El proyecto cuenta con documentación específica para diferentes audiencias:

- **[STYLE_GUIDE.md](STYLE_GUIDE.md)** - Sistema de diseño, CSS y componentes (para desarrollo frontend)
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Guía completa de contribución y setup del proyecto
- **[CLAUDE.md](CLAUDE.md)** - Documentación técnica para asistentes IA

## Contribuir

¿Quieres contribuir al proyecto? ¡Excelente! 🎉

### Formas de Contribuir

- **Proponer una charla**: Abre un [issue](https://github.com/PythonMexico/pythonCDMX/issues/new) con la plantilla "💡 Propuesta de Charla"
- **Publicar evento**: Usa la plantilla "Publicar evento en la página"
- **Reportar problema**: Crea un issue con detalles del bug
- **Mejorar código o documentación**: Crea un Pull Request siguiendo nuestro flujo de trabajo

### ⚠️ Flujo de Contribución Obligatorio

**IMPORTANTE**: Todos los Pull Requests deben seguir este flujo:

```
Tu rama → staging → main (producción)
```

1. **Crea tu rama** desde `staging`
2. **Haz tus cambios** y commits usando [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/)
3. **Abre un PR hacia `staging`** (NO hacia `main`)
4. **Completa el formulario del PR** explicando tus cambios
5. **Validación automática** en https://staging.pythoncdmx.org
6. **El equipo promoverá** los cambios a producción si todo está correcto

**⛔ NO se aceptarán Pull Requests directos a `main`**

👉 **[Ver guía completa de contribución](CONTRIBUTING.md)** para instrucciones detalladas paso a paso, setup del entorno y convenciones de código.

## Despliegue

El sitio utiliza una arquitectura de **AWS S3 + CloudFront** con dos ambientes:

### 🌐 Ambientes

#### Producción
- **URL**: https://pythoncdmx.org
- **Branch**: `main`
- **Workflow**: `.github/workflows/deploy-aws.yml`
- **Infraestructura**: S3 + CloudFront + Route53
- **Despliegue**: Automático en cada push a `main`

#### Staging (Pruebas)
- **URL**: https://staging.pythoncdmx.org
- **Branch**: `staging`
- **Workflow**: `.github/workflows/deploy-staging.yml`
- **Banner visual**: Indica ambiente de pruebas
- **Despliegue**: Automático en cada push a `staging`

### 🏗️ Infraestructura

La infraestructura está definida como código usando **Terraform**:

- **S3 Buckets**: Almacenamiento de sitio estático (producción y staging)
- **CloudFront**: CDN para distribución global
- **Route53**: DNS management
- **ACM**: Certificados SSL/TLS
- **GitHub OIDC**: Autenticación segura sin API keys

📁 Ver configuración completa en [`terraform/`](terraform/README.md)

## Enlaces de la Comunidad

### Redes Sociales
- **Telegram**: [t.me/PythonCDMX](https://t.me/PythonCDMX)
- **Meetup**: [meetup.com/python-mexico](https://www.meetup.com/python-mexico)
- **YouTube**: [@PythonMexico](https://www.youtube.com/@PythonMexico)
- **Instagram**: [@pythoncdmx](https://www.instagram.com/pythoncdmx)
- **LinkedIn**: [PythonCDMX](https://www.linkedin.com/company/pythoncdmx)

### Desarrollo
- **GitHub**: [PythonMexico/pythonCDMX](https://github.com/PythonMexico/pythonCDMX)
- **Email**: info@pythoncdmx.org

## Sedes de Eventos

- **Wizeline México** - Torre Diana, CDMX
- **UNAM Facultad de Ciencias** - Anfiteatro Alfredo Barrera
- **Diferentes espacios** - Según disponibilidad y tipo de evento

## Recursos Técnicos

- [MkDocs User Guide](https://www.mkdocs.org/user-guide/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)

## Licencia

Este proyecto está bajo la **Licencia MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Agradecimientos

### Organizadores y Voluntarios
- **Core Team** - Por la organización y coordinación
- **Voluntarios** - Por el apoyo en eventos y logística

### Sedes y Patrocinadores
- **Wizeline México** - Por hospedar nuestros meetups regulares
- **UNAM Facultad de Ciencias** - Por eventos especiales y académicos

### Comunidad
- **Ponentes** - Por compartir conocimiento y experiencias
- **Asistentes** - Por participar activamente y hacer preguntas
- **Contribuidores** - Por mejorar este sitio web continuamente

### Tecnología
- **MkDocs Material** - Por el framework de documentación
- **GitHub** - Por el hosting gratuito y herramientas de desarrollo
- **FontAwesome** - Por la iconografía

---

**¿Tienes preguntas?** Abre un [issue](https://github.com/PythonMexico/pythonCDMX/issues) o únete a nuestro [Telegram](https://t.me/PythonCDMX)
