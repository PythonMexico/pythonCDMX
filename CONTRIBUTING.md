# Guía de Contribución

¡Gracias por tu interés en contribuir a Python CDMX Charlas! Este documento te ayudará a entender cómo puedes participar en el proyecto.

## Tabla de Contenidos

- [Cómo Contribuir](#cómo-contribuir)
- [Reportar Issues](#reportar-issues)
- [Pull Requests](#pull-requests)
- [Estándares de Código](#estándares-de-código)
- [Agregar Meetups](#agregar-meetups)
- [Configuración del Entorno](#configuración-del-entorno)
- [Plantillas para Propuestas y Publicación de Meetups](#plantillas-para-propuestas-y-publicación-de-meetups)

## Cómo Contribuir

### Tipos de Contribuciones

- Reportar bugs o problemas
- Sugerir mejoras o nuevas funcionalidades
- Mejorar la documentación
- Mejorar el diseño o la experiencia de usuario
- Arreglar bugs existentes
- Desarrollar nuevas características

## Reportar Issues

### Antes de Reportar

1. Busca en issues existentes para evitar duplicados.
2. Verifica la documentación para asegurarte de que no sea un problema de configuración.
3. Prueba en la última versión de la rama `main`.

### Cómo Reportar

1. Ve a la pestaña [Issues](https://github.com/PythonMexico/pythonCDMX/issues)
2. Haz clic en "New Issue"
3. Selecciona la plantilla apropiada
4. Completa toda la información requerida

### Información Requerida

Para bugs:
- Descripción clara del problema
- Pasos para reproducirlo
- Comportamiento esperado vs actual
- Capturas de pantalla (si aplica)
- Información del sistema (OS, navegador, etc.)

Para mejoras:
- Descripción de la funcionalidad deseada
- Casos de uso
- Alternativas consideradas

## Pull Requests

### Antes de Enviar un PR

1. Haz fork del repositorio
2. Crea una rama para tu feature o fix
3. Realiza tus cambios siguiendo los estándares
4. Prueba localmente antes de enviar
5. Actualiza la documentación si es necesario

### Proceso de PR

1. Crea el PR con una descripción clara
2. Usa las plantillas disponibles
3. Vincula issues relacionados
4. Responde a feedback de los revisores
5. Mantén el PR actualizado con `main`

### Estructura del PR

```markdown
## Descripción
Breve descripción de los cambios

## Tipo de Cambio
- [ ] Bug fix
- [ ] Nueva característica
- [ ] Mejora de documentación
- [ ] Refactorización

## Cambios Realizados
- Lista de cambios específicos

## Pruebas
- [ ] Pruebas locales ejecutadas
- [ ] Documentación actualizada

## Capturas de Pantalla (si aplica)
```

## Estándares de Código

### Python

- Sigue PEP 8 para estilo de código
- Usa type hints cuando sea posible
- Documenta funciones y clases con docstrings
- Usa nombres descriptivos para variables y funciones

### Markdown

- Usa encabezados consistentes
- Listas ordenadas para pasos secuenciales
- Listas no ordenadas para elementos sin orden específico
- Usa enlaces descriptivos
- Incluye texto alternativo en imágenes

### Git

- Commits atómicos: un cambio lógico por commit
- Mensajes descriptivos y claros
- Ramas descriptivas y relacionadas con el cambio

### Ejemplo de Mensaje de Commit

```
feat: agregar página de meetup enero 2025

- Crear archivo docs/meetups/2025/enero-2025.md
- Agregar metadatos del evento
- Incluir información del ponente
- Actualizar índice de meetups 2025

Closes #123
```

## Agregar Meetups

### Estructura del Archivo

Crea archivos en `docs/meetups/YYYY/mes-YYYY.md` siguiendo la plantilla y metadatos recomendados. Incluye título, fecha, horario, lugar, ponente, temas, dificultad, idioma y enlaces relevantes (slides, video, código, etc.).

### Metadatos Requeridos

- `title` - Título de la charla
- `date` - Fecha en formato YYYY-MM-DD
- `time` - Horario del evento
- `location` - Lugar del evento
- `speaker` - Nombre del ponente
- `topics` - Lista de temas
- `difficulty` - Principiante/Intermedio/Avanzado
- `language` - Idioma de la charla

### Metadatos Opcionales

- `speaker_bio`, `speaker_company`, `speaker_twitter`, `speaker_github`, `speaker_linkedin`
- `slides`, `video`, `code`, `meetup_url`, `registration_required`, `max_attendees`

## Configuración del Entorno

### Prerrequisitos

- Python 3.8+
- Git
- Editor de código (VS Code, PyCharm, etc.)

### Configuración Inicial

```bash
# Clonar el repositorio
git clone https://github.com/PythonMexico/pythonCDMX.git
cd pythonCDMX

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor de desarrollo
mkdocs serve
```

### Comandos Útiles

```bash
# Construir sitio
mkdocs build

# Servir sitio localmente
mkdocs serve

# Validar configuración
mkdocs build --strict

# Limpiar build
rm -rf site/
```

## Áreas de Contribución

### Prioridad Alta

- Mejorar búsqueda de meetups
- Agregar filtros por tema/dificultad
- Optimizar rendimiento del sitio
- Mejorar accesibilidad

### Prioridad Media

- Agregar estadísticas de la comunidad
- Implementar sistema de comentarios
- Crear API para meetups
- Agregar notificaciones por email

### Prioridad Baja

- Agregar más temas visuales
- Implementar sistema de badges
- Crear app móvil
- Agregar integración con redes sociales

## Contacto

- Telegram: https://t.me/PythonCDMX
- Email: info@pythoncdmx.org
- Meetup: https://www.meetup.com/python-mexico

## Agradecimientos

Gracias a todas las personas que contribuyen a este proyecto. Cada aporte es valioso para la comunidad Python CDMX.

---

*Esta guía está inspirada en las mejores prácticas de proyectos open source. ¡Gracias por contribuir!*

## Plantillas para Propuestas y Publicación de Meetups

Para facilitar la colaboración y la publicación de eventos, el repositorio cuenta con dos plantillas de issues:

- **Propuesta de Charla:** Para sugerir ideas, temas o postularse como ponente, sin requerir fecha ni lugar. Puedes usar la plantilla "💡 Propuesta de Charla" al crear un nuevo issue.
- **Publicar evento en la página:** Para documentar un meetup ya confirmado y publicarlo en el sitio web. Usa la plantilla "Publicar evento en la página" cuando tengas todos los detalles del evento.

Al crear un nuevo issue en GitHub, selecciona la plantilla que corresponda según el estado de tu propuesta o evento.
