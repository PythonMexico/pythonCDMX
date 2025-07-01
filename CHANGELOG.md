# Changelog

Este archivo documenta los cambios reales y relevantes del proyecto Python CDMX Charlas, basado en el historial de commits.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/) y [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Añadido
- **Galería de Imágenes Completa**: 6 fotos profesionales de ponentes destacados + imagen de voluntario
- **Sistema de Automatización**: Scripts para detección y corrección automática de enlaces rotos
- **Estándares de Calidad**: Configuración MarkdownLint para validación automática de documentación

### Cambiado
- **Secciones de Comunidad Rediseñadas**: Ponentes y voluntarios con sistema de pestañas funcional e imágenes personales integradas
- **CSS Optimizado**: Refactorización completa de estilos con mejor organización y responsividad
- **Enlaces Corregidos**: Eliminación sistemática de enlaces rotos en toda la documentación
- **Navegación Simplificada**: Páginas de índice de meetups optimizadas sin contenido duplicado

### Eliminado
- **Contenido Obsoleto**: Archivo tags.md y elementos duplicados removidos para mejorar mantenimiento

### Arquitectura y Sistema
- **Eliminación Completa de Estilos Inline**: Migración total a CSS centralizado para separación de presentación y contenido
- **Sistema Unificado de Tarjetas**: Ponentes y voluntarios ahora usan la misma estructura base (`.volunteer-card`) con contenido diferenciado
- **Arquitectura Mantenible**: Implementación de `.volunteer-header` elimina selectores hardcodeados y facilita escalabilidad
- **Optimización CSS Significativa**: Reducción del 35% en código CSS mediante consolidación de variables y eliminación de duplicaciones
- **Sistema de Badges Comprehensivo**: 8 tipos de roles predefinidos con colores específicos para identificación visual
- **Reorganización Alfabética**: Todos los ponentes organizados alfabéticamente para mejor navegación y mantenimiento

### Impacto
- **Arquitectura Moderna**: CSS centralizado mejora dramáticamente la mantenibilidad y consistencia visual
- **Mantenimiento Simplificado**: Separación de presentación y contenido facilita actualizaciones futuras
- **Escalabilidad Mejorada**: Nueva arquitectura permite agregar contenido sin modificar estilos
- **Presentación Profesional**: Sistema unificado con imágenes personales y herramientas automatizadas

## [0.1.0]

### Añadido
- **Nueva Sección Participa**: Creada sección modular con tabs para mejor organización
- **Nuevo Voluntario**: Agregada Mónica Ortega a la lista de voluntarios destacados
- **Sistema de Tabs**: Implementado sistema de tabs en secciones de Participa para mejor navegación
- **Contenido Modular**: Separado contenido motivacional de listas de personas para mayor claridad
- **Estilos CSS Mejorados**: Añadidos estilos para tarjetas de voluntarios y ponentes
- **JavaScript Personalizado**: Agregado archivo custom.js para funcionalidad de tabs
- **Rediseño Completo de las Páginas de Meetups**: Implementado estilos modernos y atractivos
- **Nuevas Clases CSS Específicas**: Añadidas para páginas de eventos
  - `.meetup-hero` - Sección hero con gradientes y efectos visuales
  - `.meetup-banner` - Banner del evento con hover effects
  - `.event-details` - Grid responsivo para información del evento
  - `.detail-card` - Tarjetas con colores específicos por tipo (fecha, hora, lugar, etc.)
  - `.speaker-section` - Sección del ponente con animaciones flotantes
  - `.talk-description` - Descripción de la charla con efectos hover
  - `.tech-stack` - Grid de tecnologías con tarjetas interactivas
  - `.video-section` - Sección de video con botón YouTube estilizado
  - `.tags-section` - Tags de temas con gradientes y hover effects
  - `.networking-section` - Sección de networking con patrones SVG
  - `.community-links` - Enlaces de comunidad con efectos hover por plataforma
  - `.meetup-footer` - Footer del meetup
- **Efectos Visuales Mejorados**: Animaciones flotantes, efectos hover, gradientes modernos, patrones SVG sutiles, transiciones suaves
- **Diseño Completamente Responsivo**: Adaptable para móviles y tablets
- **Emojis y Iconos Mejorados**: Para mejor UX
- **Estructura HTML Más Semántica y Accesible**: Mejora en la accesibilidad
- **Campo `community_links` en los metadatos JSON de eventos para generación automática de enlaces de comunidad.**
- **Nuevo diseño visual y estructura para todos los eventos de meetups (2023, 2024, 2025).**
- **Templates de meetups (charla única y múltiples charlas) ahora idénticos al ejemplo manual: sin frontmatter, rutas absolutas para imágenes, bloques y secciones fieles al diseño manual.**
- **Community links automáticos en los eventos generados.**

### Cambiado
- **Restructuración de Participa**: Reorganizada sección Participa con tabs "Información General" y "Destacados"
- **Navegación Mejorada**: Movidas listas de ponentes y voluntarios fuera de "Reconocimientos" a sus propias secciones
- **Formato de Tarjetas**: Estandarizado formato de tarjetas para voluntarios y ponentes con estilo consistente
- **Organización de Contenido**: Separado contenido motivacional/proceso de listas de personas
- **Estructura de Archivos**: Modularizado contenido en archivos separados para mejor mantenimiento
- **Página de Julio 2025 Completamente Rediseñada**: Ejemplo de rediseño completo
- **Eliminación de Estilos Inline**: Reemplazado por clases CSS reutilizables
- **Mejora en la Legibilidad y Jerarquía Visual**: Optimización del espaciado y tipografía
- **Script `generate_meetups.py` ahora usa el campo textual `event_month_year` del JSON para mostrar el mes en texto (ej. Julio 2025).**
- **Actualización masiva de eventos de meetups con el nuevo diseño, estructura y enlaces de comunidad.**
- **Mejoras en los estilos CSS para reflejar el nuevo diseño visual de meetups y secciones.**

### Eliminado
- **Archivos Duplicados**: Eliminados archivos redundantes que duplicaban contenido:
  - `ponentes-info.md` - contenido ya incluido en `ponentes.md`
  - `ponentes-destacados.md` - contenido ya incluido en `ponentes.md` con pestañas
  - `voluntarios-info.md` - contenido ya incluido en `voluntarios.md` con pestañas
  - `voluntarios-destacados.md` - contenido ya incluido en `voluntarios.md` con pestañas
- **Contenido Duplicado**: Eliminada información duplicada entre archivos de información y listas
- **Dependencia de Snippets**: Reemplazado sistema de snippets con includes directos para mayor estabilidad
- **Eliminación de archivos de depuración y contenido redundante: ponentes, voluntarios, reconocimientos, test.**

### Corregido
- **Enlaces Internos**: Corregidos enlaces entre secciones de Participa
- **Consistencia Visual**: Asegurado estilo consistente entre secciones de voluntarios y ponentes
- **Estructura de Navegación**: Mejorada navegación entre tabs y secciones

### Technical
- **Nuevas Variables CSS**: Para consistencia en colores y efectos
- **Media Queries Optimizadas**: Para diferentes tamaños de pantalla
- **CSS Modular y Reutilizable**: Para futuras páginas de meetups

---

## [0.0.2] - 2024-06-24

### Añadido
- Lanzamiento inicial del sitio web Python CDMX Charlas
- Estructura básica de MkDocs con tema Material
- Documentación de meetups para 2023, 2024 y 2025
- Página About e información de comunidad
- Integración con redes sociales
- GitHub Actions para despliegue automático

### Cambiado
- Migrado desde formato de documentación anterior
- Actualizada identidad visual y branding
- Mejorada organización de contenido

### Corregido
- Varios problemas de documentación y enlaces
- Configuración de despliegue

---

## [0.0.1] - 2024-01-31

### Añadido
- Primer README.md y documentación básica del proyecto.
- Propuesta de charla Flask Rest Api.

---

## Notas

- Para cambios menores, agrega tus entradas bajo [Unreleased] y muévelas a una versión cuando hagas un release.
- Este changelog está basado en el historial real de commits y archivos modificados.

**Repositorio:** https://github.com/PythonMexico/pythonCDMX
