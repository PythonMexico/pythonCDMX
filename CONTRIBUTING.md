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

### Fork y Setup Inicial

```bash
# 1. Haz fork del repositorio en GitHub
# 2. Clona tu fork
git clone https://github.com/TU-USUARIO/pythonCDMX.git
cd pythonCDMX

# 3. Configura el repositorio original como upstream
git remote add upstream https://github.com/PythonMexico/pythonCDMX.git

# 4. Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# 5. Instalar dependencias
pip install -r requirements.txt

# 6. Ejecutar servidor de desarrollo
mkdocs serve
```

### Flujo de Trabajo Detallado

#### 1. Crear Rama de Trabajo

```bash
# Actualiza tu main local
git checkout main
git pull upstream main

# Crea una nueva rama descriptiva
git checkout -b feature/nueva-funcionalidad
# o
git checkout -b fix/corregir-problema
# o
git checkout -b meetup/agregar-evento-marzo-2025
```

#### 2. Realizar y Probar Cambios

```bash
# Haz tus cambios
# Prueba localmente
mkdocs serve

# Verifica que todo funcione en:
# - Modo claro y oscuro
# - Móvil y escritorio
# - Todos los enlaces
```

#### 3. Commit y Push

```bash
# Añade los cambios
git add .

# Commit con mensaje descriptivo
git commit -m "feat: agregar meetup marzo 2025 con ponentes confirmados"
# o
git commit -m "fix: corregir enlaces rotos en página de comunidad"
# o
git commit -m "style: mejorar responsive design en tarjetas de participación"

# Push a tu fork
git push origin nombre-de-tu-rama
```

#### 4. Crear Pull Request

1. Ve a tu fork en GitHub
2. Click en "Compare & pull request"
3. **Título descriptivo**: Ej. "Agregar meetup marzo 2025 - IA en producción"
4. **Descripción detallada**:
   - Qué cambios realizaste
   - Por qué son necesarios
   - Screenshots si hay cambios visuales
   - Checklist de verificación
5. Etiqueta apropiada: `meetup`, `enhancement`, `bug`, etc.

#### 5. Revisión y Merge

- El equipo revisará tu PR
- Responde a comentarios si los hay
- Una vez aprobado, será merged al proyecto principal

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

## Guidelines de Desarrollo

### Qué SÍ hacer:
- **Usar variables CSS** - No hardcodear colores o medidas
- **Probar responsive** - Verificar en móvil y escritorio
- **Seguir convenciones** - Nombres de archivos, estructura, etc.
- **Commits descriptivos** - Mensajes claros sobre los cambios
- **Screenshots en PRs** - Si hay cambios visuales
- **Usar sistema de componentes** - Reutilizar elementos existentes
- **Probar en ambos modos** - Verificar modo claro y oscuro

### Qué NO hacer:
- **Estilos inline** - Siempre usar clases CSS
- **Modificar `mkdocs.yml`** - Sin consultar primero
- **Cambios masivos** - Preferir PRs focalizados
- **Ignorar el linter** - Mantener calidad de código
- **Romper responsive** - Probar siempre en móvil
- **Hardcodear valores** - Usar variables CSS existentes

### Tipos de Issues Disponibles

#### Propuesta de Charla
Para postularte como ponente o proponer una charla

#### Publicar Evento
Para agregar un meetup confirmado a la página

#### Bug Report
Para reportar problemas o errores

#### Feature Request
Para sugerir nuevas funcionalidades

#### Documentación
Para mejorar docs o README

## Agregar Nuevo Contenido

### Nuevo Meetup

1. Crear archivo en `docs/meetups/YYYY/YYYYMM-mes.md`
2. Usar plantilla existente como referencia
3. Incluir metadatos del evento
4. Agregar descripción y detalles de charlas

### Nuevo Componente

1. Crear en `docs/components/`
2. Usar sistema de variables CSS existente
3. Seguir patrones establecidos
4. Incluir en páginas con `--8<-- "components/nombre.md"`

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
