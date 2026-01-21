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

### ⚠️ Flujo de Trabajo Obligatorio

**IMPORTANTE**: Todos los Pull Requests deben seguir este flujo:

```
Tu rama → staging → main (producción)
```

**⛔ NO SE ACEPTARÁN Pull Requests directos a `main`**

### Proceso de Contribución Paso a Paso

#### 1. Antes de Enviar un PR

1. Haz fork del repositorio
2. Crea una rama descriptiva para tu feature o fix
3. Realiza tus cambios siguiendo los estándares
4. **Asegúrate de usar Conventional Commits** (ver sección abajo)
5. Prueba localmente antes de enviar
6. Actualiza la documentación si es necesario

#### 2. Crear Pull Request hacia `staging`

1. **Crea el PR apuntando a la rama `staging`** (NO a `main`)
2. Usa las plantillas disponibles
3. **Completa TODA la información del formulario del PR**
4. Vincula issues relacionados
5. Incluye capturas de pantalla si hay cambios visuales

#### 3. Revisión en Staging

- Una vez aprobado tu PR, se hará merge a `staging`
- Se desplegará automáticamente una **versión de prueba** en:
  - 🔗 **https://staging.pythoncdmx.org**
- Esta versión incluye un banner que indica "STAGING ENVIRONMENT"
- Podrás **validar tus cambios en línea** antes de producción

#### 4. Promoción a Producción

- Si todo está correcto en staging, el equipo core:
  - Creará un PR interno de `staging` → `main`
  - Desplegará los cambios a producción (https://pythoncdmx.org)
- **Tú NO necesitas hacer este paso**, el equipo lo manejará

### Conventional Commits (Obligatorio)

**Todos los commits deben seguir el estándar Conventional Commits:**

📚 **Documentación oficial**: https://www.conventionalcommits.org/es/v1.0.0/

#### Formato Base

```
<tipo>[ámbito opcional]: <descripción>

[cuerpo opcional]

[notas al pie opcionales]
```

#### Tipos Permitidos

- **feat**: Nueva funcionalidad
- **fix**: Corrección de bugs
- **docs**: Cambios en documentación
- **style**: Cambios de formato (espacios, puntos y comas, etc.)
- **refactor**: Refactorización de código
- **test**: Agregar o modificar tests
- **chore**: Tareas de mantenimiento (dependencias, configuración, etc.)
- **perf**: Mejoras de performance

#### Ejemplos de Commits Válidos

```bash
# Nueva funcionalidad
git commit -m "feat: agregar página de meetup marzo 2025"

# Corrección de bug
git commit -m "fix: corregir enlaces rotos en página de comunidad"

# Documentación
git commit -m "docs: actualizar guía de contribución con flujo staging"

# Estilo/diseño
git commit -m "style: mejorar responsive design en tarjetas de participación"

# Refactorización
git commit -m "refactor: optimizar código de generador de meetups"

# Con ámbito
git commit -m "feat(meetups): agregar filtro por dificultad"

# Con cuerpo descriptivo
git commit -m "feat: agregar sistema de búsqueda de charlas

- Implementar búsqueda por título
- Agregar filtro por ponente
- Incluir índice de palabras clave

Closes #123"
```

#### ⚠️ Validación Automática

- El repositorio tiene **commit linting automático**
- Si tus commits no siguen Conventional Commits, el CI **fallará**
- Asegúrate de formatear correctamente tus mensajes

### Estructura del PR (Plantilla)

**Por favor, completa TODA esta información:**

```markdown
## 📝 Descripción
Breve descripción de los cambios realizados

## 🏷️ Tipo de Cambio
- [ ] 🐛 Bug fix (corrección de errores)
- [ ] ✨ Nueva característica (feature)
- [ ] 📚 Mejora de documentación
- [ ] ♻️ Refactorización
- [ ] 🎨 Cambios de diseño/estilo
- [ ] 📅 Nuevo meetup/evento

## 🔧 Cambios Realizados
- Lista detallada de cambios específicos
- Incluye archivos modificados si es relevante
- Menciona componentes afectados

## ✅ Checklist de Verificación
- [ ] He probado los cambios localmente (`mkdocs serve`)
- [ ] Los commits siguen Conventional Commits
- [ ] He actualizado la documentación (si aplica)
- [ ] He probado en modo claro y oscuro
- [ ] He probado en dispositivos móviles
- [ ] Los enlaces funcionan correctamente
- [ ] Las imágenes tienen texto alternativo
- [ ] No hay errores en la consola del navegador

## 📸 Capturas de Pantalla (si aplica)
Agrega screenshots si hay cambios visuales

### Antes
[Imagen del estado anterior]

### Después
[Imagen con los nuevos cambios]

## 🔗 Issues Relacionados
Closes #[número del issue]
Relates to #[número del issue]

## 📋 Notas Adicionales
Cualquier información adicional relevante para los revisores
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

- **Commits atómicos**: Un cambio lógico por commit
- **Conventional Commits obligatorio**: Todos los commits deben seguir el estándar
- **Mensajes descriptivos**: Usa el formato `tipo(ámbito): descripción`
- **Ramas descriptivas**: Nombres relacionados con el cambio (ej: `feat/nueva-busqueda`, `fix/enlaces-rotos`)

Ver la sección [Conventional Commits](#conventional-commits-obligatorio) para ejemplos detallados.

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

- Python 3.11+
- Git
- [uv](https://docs.astral.sh/uv/) (gestor de paquetes y proyectos Python - recomendado) o pip
- Editor de código (VS Code, PyCharm, etc.)

### Fork y Setup Inicial

1. Haz un fork del repositorio en Github
2. Clona tu fork usando `git clone https://github.com/${TU_USUARIO}/pythonCDMX.git`, haciéndolo de esta manera, se registrarán automáticamente `origin` y `upstream` 

#### Ejecutar usando UV (Recomendado)

```bash
# Para instalar las dependencias
uv sync
# Ejecuta el programa con
uv run mkdocs serve
```

#### Ejecutar usando Pip+Venv (Tradicional)

```bash
# Crea el entorno virtual
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor de desarrollo
mkdocs serve
```

### Flujo de Trabajo Detallado

#### 1. Crear Rama de Trabajo

```bash
# Actualiza tu rama staging local desde upstream
git checkout staging
git pull upstream staging

# Crea una nueva rama descriptiva desde staging
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
# ✅ Modo claro y oscuro
# ✅ Móvil y escritorio
# ✅ Todos los enlaces funcionan
# ✅ Imágenes se cargan correctamente
# ✅ No hay errores en consola
```

#### 3. Commit y Push (usando Conventional Commits)

```bash
# Añade los cambios
git add .

# Commit con mensaje siguiendo Conventional Commits
git commit -m "feat: agregar meetup marzo 2025 con ponentes confirmados"
# o
git commit -m "fix: corregir enlaces rotos en página de comunidad"
# o
git commit -m "docs: actualizar guía de contribución"
# o
git commit -m "style: mejorar responsive design en tarjetas de participación"

# Push a tu fork
git push origin nombre-de-tu-rama
```

#### 4. Crear Pull Request hacia `staging`

1. Ve a tu fork en GitHub
2. Click en "Compare & pull request"
3. **⚠️ IMPORTANTE**: Asegúrate que el PR apunte a `staging` (NO a `main`)
4. **Título descriptivo**: Sigue Conventional Commits en el título
   - Ejemplo: `feat: agregar meetup marzo 2025 - IA en producción`
5. **Completa el formulario del PR** con TODA la información:
   - Descripción de cambios
   - Tipo de cambio (checkbox)
   - Lista de cambios realizados
   - Checklist de verificación completada
   - Screenshots si hay cambios visuales
   - Issues relacionados
6. Etiqueta apropiada: `meetup`, `enhancement`, `bug`, `documentation`, etc.

#### 5. Revisión en Staging

- El equipo revisará tu PR
- Responde a comentarios si los hay
- Una vez aprobado, se hará **merge a `staging`**
- El sitio se desplegará automáticamente en **https://staging.pythoncdmx.org**
- Podrás ver tus cambios en línea y validarlos

#### 6. Promoción a Producción (Automático)

- Si todo está correcto en staging, el equipo core:
  - Creará un PR de `staging` → `main`
  - Tus cambios se desplegarán a producción
- **No necesitas hacer nada más**, el equipo manejará este paso

### Comandos Útiles

```bash
# Construir sitio
uv run mkdocs build

# Servir sitio localmente
uv run mkdocs serve

# Validar configuración
uv run mkdocs build --strict

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
