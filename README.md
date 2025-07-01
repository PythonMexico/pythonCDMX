# Python CDMX - Sitio Web de la Comunidad

> *"Vine por el código, me quedé por la comunidad"*

Sitio web oficial de la comunidad Python CDMX, construido con **MkDocs Material** y diseño **Material Design** optimizado. Documentamos todos nuestros meetups, charlas y eventos, conectando a la comunidad Python de la Ciudad de México.

[![Despliegue automático](https://github.com/PythonMexico/pythonCDMX/actions/workflows/deploy.yml/badge.svg)](https://github.com/PythonMexico/pythonCDMX/actions/workflows/deploy.yml)
[![Sitio Web](https://img.shields.io/badge/sitio-pythoncdmx.org-4CAF50)](https://pythonmexico.github.io/pythonCDMX/)

## Características Principales

- **Material Design moderno** - Interfaz limpia con modo claro/oscuro automático
- **Completamente responsive** - Optimizado para móvil, tablet y escritorio
- **Búsqueda avanzada** - Encuentra charlas por tema, ponente o contenido
- **Videos integrados** - Acceso directo a nuestras charlas en YouTube
- **CSS optimizado** - Sistema de variables centralizadas y componentes reutilizables
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
│   │   └── custom.css            # Estilos optimizados (~450 líneas)
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
- **Variables centralizadas** - Fácil personalización de colores y espaciado
- **Sistema de botones** - `.btn-primary`, `.btn`, `.btn-nav`
- **Tarjetas de participación** - Design centrado con iconos grandes
- **Enlaces de comunidad** - Colores oficiales por plataforma
- **Responsive design** - Breakpoint único en 768px

## Contribuir

¿Quieres contribuir al proyecto? ¡Excelente! 🎉

- **Proponer una charla**: Abre un [issue](https://github.com/PythonMexico/pythonCDMX/issues/new) con la plantilla "💡 Propuesta de Charla"
- **Publicar evento**: Usa la plantilla "Publicar evento en la página"
- **Reportar problema**: Crea un issue con detalles del bug
- **Mejorar documentación**: Los PRs son bienvenidos

👉 **[Ver guía completa de contribución](CONTRIBUTING.md)** para proceso detallado, setup del entorno y guidelines.

## Despliegue

El sitio se despliega automáticamente a **GitHub Pages** en cada push a `main`:

- **URL de producción**: https://pythonmexico.github.io/pythonCDMX/
- **Workflow**: `.github/workflows/deploy.yml`
- **Rama de despliegue**: `gh-pages` (automática)

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
