# Python CDMX Charlas

Sitio web oficial de la comunidad Python CDMX, construido con MkDocs y Material for MkDocs. Aquí documentamos todos nuestros meetups, charlas y eventos desde 2023.

## Características

- Responsive Design: Optimizado para todos los dispositivos
- Búsqueda avanzada: Encuentra charlas por tema, ponente o contenido
- Tema personalizado: Colores inspirados en nuestro logo
- Estadísticas de la comunidad
- Videos integrados: Acceso directo a nuestras charlas en YouTube
- Modo claro/oscuro
- Despliegue automático con GitHub Actions

## Estructura del proyecto

```
pythonCDMX/
├── docs/                # Documentación y contenido principal
│   ├── css/             # Estilos personalizados
│   ├── meetups/         # Páginas de meetups por año
│   ├── index.md         # Página principal
│   └── about.md         # Sobre la comunidad
├── scripts/             # Herramientas y utilidades
├── .github/workflows/   # Automatización con GitHub Actions
├── mkdocs.yml           # Configuración de MkDocs
├── requirements.txt     # Dependencias
└── README.md            # Este archivo
```

## Instalación y desarrollo

### Prerrequisitos

- Python 3.8 o superior
- pip

### Instalación rápida

```bash
git clone https://github.com/PythonMexico/pythonCDMX.git
cd pythonCDMX
pip install -r requirements.txt
```

### Servidor local

```bash
mkdocs serve
```
Abre tu navegador en http://localhost:8000

### Construcción para producción

```bash
mkdocs build
```
El sitio se generará en la carpeta `site/`.

## Agregar nuevos meetups

1. Crea un archivo en `docs/meetups/YYYY/mes-YYYY.md`
2. Usa la plantilla de meetup
3. Agrega metadatos y contenido
4. Actualiza los índices si es necesario

¿Tienes muchos datos? Usa el script de migración:

```bash
python scripts/migrate_to_markdown.py
```

## Despliegue en GitHub Pages

Cada vez que haces push a la rama `main`, el sitio se actualiza automáticamente en:
https://pythonmexico.github.io/pythonCDMX/

## Contribuir

- Reporta problemas o sugiere mejoras en Issues: https://github.com/PythonMexico/pythonCDMX/issues
- Haz un fork, crea una rama, haz tus cambios y envía un Pull Request
- Sigue las convenciones de nombres y prueba localmente antes de enviar

### Plantillas de Issues para Meetups

- Si quieres **proponer una charla o postularte como ponente**, usa la plantilla "💡 Propuesta de Charla" al crear un nuevo issue.
- Si quieres **publicar un evento confirmado en la página**, usa la plantilla "Publicar evento en la página" y proporciona toda la información del meetup.

## Recursos útiles

- MkDocs User Guide: https://www.mkdocs.org/user-guide/
- Material for MkDocs: https://squidfunk.github.io/mkdocs-material/
- PyMdown Extensions: https://facelessuser.github.io/pymdown-extensions/

## Sedes de eventos

- Wizeline México: Torre Diana, CDMX
- UNAM Facultad de Ciencias: Anfiteatro Alfredo Barrera

## Enlaces de la comunidad

- Telegram: https://t.me/PythonCDMX
- Meetup: https://www.meetup.com/python-mexico
- YouTube: https://www.youtube.com/@PythonMexico
- GitHub: https://github.com/PythonMexico/pythonCDMX
- Twitter: https://twitter.com/PythonMexico
- Email: info@pythoncdmx.org

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

## Agradecimientos

- Wizeline México - Por hospedar nuestros meetups
- UNAM Facultad de Ciencias - Por eventos especiales
- Todos los ponentes - Por compartir su conocimiento
- Comunidad Python CDMX - Por su participación activa

---

Última actualización: {{ git_revision_date_localized }}
