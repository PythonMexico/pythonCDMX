# Guía de Contribución 🤝

¡Gracias por tu interés en contribuir a Python CDMX Charlas! Este documento te ayudará a entender cómo puedes participar en el proyecto.

## 📋 Tabla de Contenidos

- [Cómo Contribuir](#cómo-contribuir)
- [Reportar Issues](#reportar-issues)
- [Pull Requests](#pull-requests)
- [Estándares de Código](#estándares-de-código)
- [Agregar Meetups](#agregar-meetups)
- [Configuración del Entorno](#configuración-del-entorno)

## 🚀 Cómo Contribuir

### Tipos de Contribuciones

- 🐛 **Reportar bugs** - Ayúdanos a encontrar y arreglar problemas
- 💡 **Sugerir mejoras** - Propón nuevas características o mejoras
- 📝 **Mejorar documentación** - Ayuda a que la documentación sea más clara
- 🎨 **Mejorar el diseño** - Sugiere mejoras visuales o de UX
- 🔧 **Arreglar bugs** - Implementa soluciones para problemas conocidos
- ✨ **Nuevas características** - Desarrolla nuevas funcionalidades

## 🐛 Reportar Issues

### Antes de Reportar

1. **Busca en issues existentes** - Es posible que tu problema ya haya sido reportado
2. **Verifica la documentación** - Asegúrate de que no sea un problema de configuración
3. **Prueba en la última versión** - Confirma que el problema persiste en `main`

### Cómo Reportar

1. Ve a la pestaña [Issues](https://github.com/PythonMexico/python-cdmx-page/issues)
2. Haz clic en "New Issue"
3. Selecciona la plantilla apropiada
4. Completa toda la información requerida

### Información Requerida

Para **bugs**:
- Descripción clara del problema
- Pasos para reproducir
- Comportamiento esperado vs actual
- Capturas de pantalla (si aplica)
- Información del sistema (OS, navegador, etc.)

Para **mejoras**:
- Descripción de la funcionalidad deseada
- Casos de uso
- Alternativas consideradas

## 🔄 Pull Requests

### Antes de Enviar un PR

1. **Fork el repositorio**
2. **Crea una rama** para tu feature/fix
3. **Haz tus cambios** siguiendo los estándares
4. **Prueba localmente** antes de enviar
5. **Actualiza la documentación** si es necesario

### Proceso de PR

1. **Crea el PR** con una descripción clara
2. **Usa las plantillas** disponibles
3. **Vincula issues** relacionados
4. **Responde a feedback** rápidamente
5. **Mantén el PR actualizado** con `main`

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

## 📏 Estándares de Código

### Python

- **PEP 8** - Sigue las convenciones de estilo
- **Type hints** - Usa anotaciones de tipo cuando sea posible
- **Docstrings** - Documenta funciones y clases
- **Nombres descriptivos** - Usa nombres claros para variables y funciones

### Markdown

- **Encabezados consistentes** - Usa `#` para títulos principales
- **Listas ordenadas** - Para pasos secuenciales
- **Listas no ordenadas** - Para elementos sin orden específico
- **Enlaces descriptivos** - Usa texto descriptivo para enlaces
- **Imágenes con alt text** - Siempre incluye texto alternativo

### Git

- **Commits atómicos** - Un cambio lógico por commit
- **Mensajes descriptivos** - Usa el formato convencional
- **Ramas descriptivas** - Nombra las ramas claramente

### Ejemplo de Mensaje de Commit

```
feat: agregar página de meetup enero 2025

- Crear archivo docs/meetups/2025/enero-2025.md
- Agregar metadatos del evento
- Incluir información del ponente
- Actualizar índice de meetups 2025

Closes #123
```

## 📅 Agregar Meetups

### Estructura del Archivo

Crea archivos en `docs/meetups/YYYY/mes-YYYY.md`:

```markdown
---
title: "Título de la Charla"
date: 2025-01-15
time: "18:30 - 21:00"
location: "Wizeline México"
address: "Torre Diana, Piso 32, CDMX"
speaker: "Nombre del Ponente"
speaker_bio: "Breve biografía del ponente"
speaker_company: "Empresa del ponente"
speaker_twitter: "@usuario"
speaker_github: "usuario"
speaker_linkedin: "usuario"
topics: ["Python", "Web Development", "AI"]
difficulty: "Intermedio"
language: "Español"
slides: "https://slides.com/usuario/charla"
video: "https://youtube.com/watch?v=VIDEO_ID"
code: "https://github.com/usuario/repo"
meetup_url: "https://meetup.com/python-mexico/events/123"
registration_required: true
max_attendees: 50
---

## Descripción

Descripción detallada de la charla...

## Temas a Cubrir

- Tema 1
- Tema 2
- Tema 3

## Requisitos Previos

- Conocimiento básico de Python
- Familiaridad con conceptos de web

## Material Adicional

- [Enlace 1](url)
- [Enlace 2](url)

## Galería

![Foto del evento](ruta/a/la/imagen.jpg)

## Agradecimientos

Agradecimientos especiales a...
```

### Metadatos Requeridos

- `title` - Título de la charla
- `date` - Fecha en formato YYYY-MM-DD
- `time` - Horario del evento
- `location` - Lugar del evento
- `speaker` - Nombre del ponente
- `topics` - Lista de temas (array)
- `difficulty` - Principiante/Intermedio/Avanzado
- `language` - Idioma de la charla

### Metadatos Opcionales

- `speaker_bio` - Biografía del ponente
- `speaker_company` - Empresa del ponente
- `speaker_twitter` - Twitter del ponente
- `speaker_github` - GitHub del ponente
- `speaker_linkedin` - LinkedIn del ponente
- `slides` - Enlace a presentación
- `video` - Enlace a video
- `code` - Enlace a código
- `meetup_url` - Enlace al evento en Meetup
- `registration_required` - Si requiere registro
- `max_attendees` - Máximo de asistentes

## 🛠️ Configuración del Entorno

### Prerrequisitos

- Python 3.8+
- Git
- Editor de código (VS Code, PyCharm, etc.)

### Configuración Inicial

```bash
# Clonar el repositorio
git clone https://github.com/PythonMexico/python-cdmx-page.git
cd python-cdmx-page

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

## 🎯 Áreas de Contribución

### Prioridad Alta

- [ ] Mejorar búsqueda de meetups
- [ ] Agregar filtros por tema/dificultad
- [ ] Optimizar rendimiento del sitio
- [ ] Mejorar accesibilidad

### Prioridad Media

- [ ] Agregar estadísticas de la comunidad
- [ ] Implementar sistema de comentarios
- [ ] Crear API para meetups
- [ ] Agregar notificaciones por email

### Prioridad Baja

- [ ] Agregar más temas visuales
- [ ] Implementar sistema de badges
- [ ] Crear app móvil
- [ ] Agregar integración con redes sociales

## 📞 Contacto

- **Telegram:** [@PythonCDMX](https://t.me/PythonCDMX)
- **Email:** info@pythoncdmx.org
- **Meetup:** [Python México](https://www.meetup.com/python-mexico)

## 🙏 Agradecimientos

Gracias a todos los contribuidores que hacen posible este proyecto. Cada contribución, sin importar su tamaño, es valiosa para la comunidad Python CDMX.

---

*Esta guía está inspirada en las mejores prácticas de proyectos open source. ¡Gracias por contribuir! 🐍*
