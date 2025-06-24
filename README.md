# Python CDMX Charlas 🐍

Sitio web oficial de la comunidad Python CDMX, construido con MkDocs y Material for MkDocs. Este sitio documenta todos nuestros meetups, charlas y eventos desde 2023.

## 🚀 Características

- **📱 Responsive Design** - Optimizado para todos los dispositivos
- **🔍 Búsqueda Avanzada** - Encuentra charlas por tema, ponente o contenido
- **🎨 Tema Personalizado** - Colores del logo Python CDMX (#269f46, #000000, #e32f42)
- **📊 Estadísticas** - Métricas de la comunidad en tiempo real
- **🎬 Videos Integrados** - Enlaces directos a YouTube
- **🌙 Modo Oscuro** - Soporte para tema claro y oscuro
- **⚡ Despliegue Automático** - GitHub Actions para GitHub Pages

## 🏗️ Estructura del Proyecto

```
python-cdmx-charlas/
├── docs/                          # Documentación MkDocs
│   ├── css/                       # Estilos personalizados
│   │   └── custom.css
│   │
│   ├── meetups/                   # Páginas de meetups
│   │   ├── index.md              # Página principal de meetups
│   │   ├── 2025/                 # Meetups 2025
│   │   ├── 2024/                 # Meetups 2024
│   │   └── 2023/                 # Meetups 2023
│   │
│   ├── index.md                  # Página principal
│   └── about.md                  # Acerca de
│
├── scripts/                       # Scripts de utilidad
│   └── migrate_to_markdown.py    # Migración de datos
│
├── .github/workflows/            # GitHub Actions
│   └── deploy.yml
│
├── mkdocs.yml                    # Configuración MkDocs
│
├── requirements.txt              # Dependencias Python
│
└── README.md                     # Este archivo
```

## 🛠️ Instalación y Desarrollo

### Prerrequisitos

- Python 3.8+
- pip

### Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/PythonMexico/python-cdmx-page.git
   cd python-cdmx-page
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar servidor de desarrollo**
   ```bash
   mkdocs serve
   ```

4. **Abrir en navegador**
   ```
   http://localhost:8000
   ```

### Construcción para Producción

```bash
mkdocs build
```

El sitio se construirá en el directorio `site/`.

## 📝 Agregar Nuevos Meetups

### Método 1: Manual (Recomendado)

1. Crear archivo en `docs/meetups/YYYY/mes-YYYY.md`
2. Usar la plantilla de meetup existente
3. Incluir metadatos y contenido
4. Actualizar índices correspondientes

### Método 2: Migración Automática

Si tienes datos en formato de texto:

```bash
python scripts/migrate_to_markdown.py
```

## 🎨 Personalización

### Colores del Tema

Los colores están definidos en `docs/css/custom.css`:

```css
:root {
  --python-green: #269f46;
  --python-black: #000000;
  --python-red: #e32f42;
}
```

### Configuración MkDocs

Edita `mkdocs.yml` para modificar:

- Título y descripción del sitio
- Navegación
- Plugins
- Enlaces sociales
- Configuración del tema

## 🚀 Despliegue

### GitHub Pages (Automático)

El sitio se despliega automáticamente a GitHub Pages cuando se hace push a `main`.

**Configuración requerida:**
1. Habilitar GitHub Pages en el repositorio
2. Configurar fuente como "GitHub Actions"
3. El workflow `.github/workflows/deploy.yml` se ejecutará automáticamente

### Despliegue Manual

```bash
# Construir sitio
mkdocs build

# Subir a servidor web
rsync -av site/ user@server:/path/to/web/root/
```

## 📊 Estadísticas del Sitio

- **Total meetups:** 23+ (2023-2025)
- **Ponentes únicos:** 15+
- **Temas principales:** AI, Web Dev, DevOps, Data Science
- **Videos disponibles:** 20+

## 🤝 Contribuir

### Reportar Issues

1. Ve a [Issues](https://github.com/PythonMexico/python-cdmx-page/issues)
2. Crea un nuevo issue
3. Describe el problema o sugerencia

### Pull Requests

1. Fork el repositorio
2. Crea una rama para tu feature
3. Haz tus cambios
4. Envía un Pull Request

### Guías de Contribución

- Usa Markdown para contenido
- Sigue las convenciones de nombres
- Incluye metadatos completos
- Prueba localmente antes de enviar

## 📚 Recursos Útiles

### Documentación MkDocs
- [MkDocs User Guide](https://www.mkdocs.org/user-guide/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)

### Herramientas de Desarrollo
- [Python Markdown](https://python-markdown.github.io/)
- [GitHub Pages](https://pages.github.com/)
- [GitHub Actions](https://docs.github.com/en/actions)

## 🏢 Lugares de Eventos

### Wizeline México
- **Dirección:** Torre Diana, Piso 32, CDMX
- **Horario:** 18:30 - 21:00
- **Acceso:** Registro con identificación oficial

### UNAM Facultad de Ciencias
- **Dirección:** Anfiteatro Alfredo Barrera
- **Horario:** 16:00 - 19:00
- **Eventos:** Especiales

## 🔗 Enlaces de la Comunidad

- [📱 Telegram](https://t.me/PythonCDMX) - Grupo principal
- [📅 Meetup](https://www.meetup.com/python-mexico) - Eventos oficiales
- [🎥 YouTube](https://www.youtube.com/@PythonMexico) - Transmisiones
- [🐙 GitHub](https://github.com/python-cdmx) - Código y recursos
- [🐦 Twitter](https://twitter.com/PythonMexico) - Noticias
- [📧 Email](mailto:info@pythoncdmx.org) - Contacto oficial

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- **Wizeline México** - Por hospedar nuestros meetups
- **UNAM Facultad de Ciencias** - Por eventos especiales
- **Todos los ponentes** - Por compartir su conocimiento
- **Comunidad Python CDMX** - Por su participación activa

---

*Última actualización: {{ git_revision_date_localized }}*
