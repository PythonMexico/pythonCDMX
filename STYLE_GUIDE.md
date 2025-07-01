# Guía de Estilos - Python CDMX

> Documentación completa del sistema de diseño, arquitectura CSS y componentes del sitio web Python CDMX

Esta guía documenta el sistema de diseño del sitio web de Python CDMX, construido con **MkDocs Material** siguiendo una **arquitectura variables-first** y principios de **Material Design**.

## Tabla de Contenidos

- [Filosofía de Diseño](#filosofía-de-diseño)
- [Arquitectura CSS](#arquitectura-css)
- [Sistema de Variables](#sistema-de-variables)
- [Componentes](#componentes)
- [Sistema Unificado de Tarjetas](#sistema-unificado-de-tarjetas)
- [Layout y Responsive](#layout-y-responsive)
- [Buenas Prácticas](#buenas-prácticas)
- [Troubleshooting](#troubleshooting)

## Filosofía de Diseño

### Principios Fundamentales

1. **Variables-First** - Todo color, espaciado y transición debe usar variables CSS
2. **Mobile-First** - Diseño responsive con breakpoint único en 768px
3. **Sistema Unificado** - Componentes reutilizables con estructura consistente
4. **Zero `!important`** - Arquitectura CSS limpia con especificidad apropiada
5. **Compatibilidad Automática** - Modo claro/oscuro usando variables de MkDocs Material

### Lema de la Comunidad

> *"Vine por el código, me quedé por la comunidad"*

Este lema es central y se destaca en todo el sitio usando el componente `.community-motto`.

## Arquitectura CSS

### Estructura del Archivo CSS

El archivo `docs/css/custom.css` (~1466 líneas) está organizado en 13 secciones lógicas:

1. **Variables CSS personalizadas** - 18+ variables centralizadas
2. **Sección Hero** - Página principal y logos
3. **Sistema de botones** - 4 variantes de botones
4. **Tarjetas y grillas** - Componentes base
5. **Tarjetas de voluntarios** - Sistema unificado
6. **Tarjetas de comunidades aliadas** - Partners y alianzas
7. **Enlaces de comunidad** - Redes sociales con colores de marca
8. **Lema de la comunidad** - Componente destacado
9. **Navegación y secciones especiales** - Navegación rápida
10. **Iconografía** - FontAwesome 6.4.0
11. **Animaciones** - Transiciones y efectos
12. **Media queries responsivas** - Breakpoint único
13. **Utilidades y helpers** - Clases auxiliares

### Configuración en MkDocs

```yaml
# mkdocs.yml
theme:
  palette:
    - scheme: default
      primary: green
      accent: green
    - scheme: slate
      primary: green
      accent: green

extra_css:
  - css/custom.css
```

## Sistema de Variables

### Variables Principales

```css
:root {
  /* Colores principales */
  --python-green: #4CAF50;
  --python-green-dark: #45a049;
  --python-white: #ffffff;

  /* Radios y espaciado */
  --button-radius: 3.125rem;
  --card-radius: 0.75rem;

  /* Transiciones estándar */
  --transition-base: all 0.3s ease;
  --transition-smooth: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
```

### Colores de Redes Sociales

```css
:root {
  --telegram-color: #0088cc;
  --meetup-color: #ed1c40;
  --youtube-color: #ff0000;
  --github-color: #333333;
  --instagram-color: #e4405f;
  --linkedin-color: #0077b5;
}
```

### Colores de Badges y Roles

```css
:root {
  /* Colores de badges */
  --badge-ambassador: #2E7D32;
  --badge-organizer: #1565C0;
  --badge-production: #E65100;
  --badge-host: #6A1B9A;
  --badge-technical: #37474F;
  --badge-support: #3E2723;
  --badge-global: #AD1457;
  --badge-strategic: #283593;
}
```

### Colores de Años y Categorías

```css
:root {
  /* Colores de años y especialización */
  --year-2024-color: #2196F3;
  --year-2024-hover: #1976D2;
  --year-2023-color: #FF9800;
  --year-2023-hover: #F57C00;
}
```

### Patrón de Uso

```css
.nuevo-componente {
  background: var(--python-green);
  border-radius: var(--card-radius);
  transition: var(--transition-base);
  color: var(--python-white);
  /* Usar variables de badges para roles */
  border-left: 4px solid var(--badge-technical);
}

.nuevo-componente:hover {
  background: var(--python-green-dark);
  transform: translateY(-2px);
}
```

## Componentes

### Sistema de Botones

#### `.btn-primary` - Botón Principal Verde

```css
.upcoming-btn,
.btn,
.btn-primary,
.participation-card a,
.year-card a {
  background: var(--python-green);
  color: var(--python-white);
  padding: 0.75rem 1.5rem;
  border-radius: var(--button-radius);
  transition: var(--transition-base);
}
```

**Uso:**
```html
<a href="/meetups/" class="btn-primary">Ver Todos los Meetups</a>
```

#### `.btn-nav` - Botón de Navegación Discreto

```css
.btn-nav {
  background: transparent;
  color: var(--md-default-fg-color--light);
  border: 1px solid var(--md-default-fg-color--lightest);
  padding: 0.5rem 1rem;
  border-radius: 1.5rem;
  min-width: 140px;
}
```

**Uso:**
```html
<a href="/meetups/2025/" class="btn-nav">
  <i class="fas fa-calendar"></i> Meetups 2025
</a>
```

### Enlaces de Comunidad

#### Estructura HTML

```html
<div class="community-links">
  <a href="https://t.me/PythonCDMX" class="community-link telegram">
    <i class="fab fa-telegram"></i> Telegram
  </a>
  <a href="https://www.meetup.com/python-mexico" class="community-link meetup">
    <i class="fas fa-calendar"></i> Meetup
  </a>
  <a href="https://www.youtube.com/@PythonMexico" class="community-link youtube">
    <i class="fab fa-youtube"></i> YouTube
  </a>
</div>
```

#### CSS con Colores por Plataforma

```css
.community-links {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin: 2rem 0;
}

.community-link.telegram:hover {
  background: var(--telegram-color);
  color: white;
}

.community-link.meetup:hover {
  background: var(--meetup-color);
  color: white;
}
```

### Tarjetas de Participación

#### Estructura HTML

```html
<div class="participation-grid">
  <div class="participation-card participation-ponente">
    <h3><i class="fas fa-microphone"></i> Ser Ponente</h3>
    <p>Comparte tu conocimiento con la comunidad Python CDMX...</p>
    <a href="/comunidad/ponentes/" class="btn-primary">Proponer Charla</a>
  </div>
  <div class="participation-card participation-voluntario">
    <h3><i class="fas fa-hands-helping"></i> Ser Voluntario</h3>
    <p>Ayuda a organizar eventos y apoyar a la comunidad...</p>
    <a href="/comunidad/voluntarios/" class="btn-primary">Únete al Equipo</a>
  </div>
</div>
```

#### CSS Grid Responsive

```css
.participation-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.participation-card {
  padding: 2rem;
  min-height: 200px;
  text-align: center;
  border-radius: var(--card-radius);
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lightest);
}

/* Especialización por tipo */
.participation-ponente {
  border-left: 4px solid var(--python-green);
}

.participation-voluntario {
  border-left: 4px solid var(--year-2024-color);
}
```

### Lema de la Comunidad

```css
.community-motto {
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: var(--card-radius);
  font-size: 1.5rem;
  font-style: italic;
  font-weight: 300;
  margin: 2rem auto;
  max-width: 600px;
  padding: 2rem;
  position: relative;
  text-align: center;
  color: var(--md-primary-fg-color);
}

.community-motto::before,
.community-motto::after {
  content: '"';
  font-size: 3rem;
  color: var(--python-green);
  position: absolute;
}

.community-motto::before {
  top: -10px;
  left: 20px;
}

.community-motto::after {
  bottom: -40px;
  right: 20px;
}
```

### Comunidades Aliadas

#### Estructura HTML

```html
<div class="communities-grid">
  <div class="community-card">
    <img src="/images/comunidades/partner-logo.png" alt="Community Partner">
    <h4><i class="fas fa-users"></i> Nombre de la Comunidad</h4>
    <p>Descripción breve de la comunidad aliada</p>
  </div>
</div>
```

#### CSS con Efectos Avanzados

```css
.communities-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.community-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 2rem 1.5rem;
  background: var(--md-default-bg-color);
  border: 2px solid var(--md-default-fg-color--lightest);
  border-radius: var(--card-radius);
  transition: var(--transition-smooth);
  position: relative;
  overflow: hidden;
}

.community-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(76, 175, 80, 0.1), transparent);
  transition: var(--transition-smooth);
}

.community-card:hover::before {
  left: 100%;
}

.community-card img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 1rem;
  border: 3px solid var(--md-default-fg-color--lightest);
  transition: var(--transition-base);
}

.community-card:hover img {
  border-color: var(--python-green);
  transform: scale(1.05);
}
```

## Sistema Unificado de Tarjetas

### Arquitectura Unificada

Voluntarios y ponentes usan la **misma estructura** `.volunteer-card` pero con contenido diferenciado:

- **Voluntarios**: Enfoque en contribuciones comunitarias y roles organizacionales
- **Ponentes**: Enfoque en especialidades técnicas y charlas recientes

### Estructura HTML Base

```html
### Nombre de la Persona {.volunteer-header}

<div class="volunteer-card">
  <div class="card-header">
    <div class="card-info">
      <h3 class="card-title">Nombre de la Persona</h3>
      <p class="card-subtitle">Rol/Empresa descripción</p>
      <div class="badges-container">
        <!-- Para Voluntarios -->
        <span class="badge ambassador">Embajador</span>
        <span class="badge organizer">Organizador</span>
        <!-- Para Ponentes -->
        <span class="badge technical">DevOps</span>
        <span class="badge development">Desarrollo</span>
      </div>
    </div>
    <div class="avatar-section">
      <img src="/images/ponentes/avatar.jpg" alt="Persona" class="volunteer-avatar">
      <div class="social-icons">
        <a href="#" class="social-icon linkedin"><i class="fab fa-linkedin"></i></a>
        <a href="#" class="social-icon github"><i class="fab fa-github"></i></a>
      </div>
    </div>
  </div>
  <div class="card-content">
    <div class="card-role">
      <span class="role-title">ESPECIALIDADES TÉCNICAS</span>
      <span class="role-description">Lista de especialidades técnicas</span>
      <strong>Charlas recientes:</strong>
      <ul>
        <li>Contenido item 1</li>
        <li>Contenido item 2</li>
      </ul>
    </div>
  </div>
</div>
```

### CSS del Sistema Unificado

```css
.volunteer-card {
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: var(--card-radius);
  padding: 2rem;
  margin-bottom: 2rem;
  transition: var(--transition-base);
}

.volunteer-card .card-header {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 2rem;
  align-items: start;
  margin-bottom: 1.5rem;
}

.volunteer-card .volunteer-avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid var(--md-primary-fg-color--light);
  transition: var(--transition-base);
}
```

### Sistema de Badges

```css
.volunteer-card .badge {
  padding: 0.125rem 0.5rem;
  border-radius: 0.75rem;
  font-size: 0.625rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}

.volunteer-card .badge.ambassador {
  background: rgba(76, 175, 80, 0.15);
  color: var(--badge-ambassador);
  border: 1px solid rgba(76, 175, 80, 0.3);
}

.volunteer-card .badge.technical {
  background: rgba(96, 125, 139, 0.15);
  color: var(--badge-technical);
  border: 1px solid rgba(96, 125, 139, 0.3);
}
```

### Diferenciación de Contenido

#### Para Voluntarios
```html
<span class="role-title">COMMUNITY ROLE TITLE</span>
<span class="role-description">Community role description</span>
<strong>Contribuciones principales:</strong>
<ul>
  <li>Organización y planeación de meetups</li>
  <li>Representación en otros espacios</li>
</ul>
```

#### Para Ponentes
```html
<span class="role-title">ESPECIALIDADES TÉCNICAS</span>
<span class="role-description">DevOps, Docker, Kubernetes, CI/CD</span>
<strong>Charlas recientes:</strong>
<ul>
  <li><a href="/meetups/2025/202507-julio/">"Título de la charla" (Julio 2025)</a></li>
</ul>
```

### Organización de Imágenes

- **Voluntarios**: `/images/voluntarios/filename.jpg`
- **Ponentes**: `/images/ponentes/filename.jpg`
- **Comunidades**: `/images/comunidades/filename.png`

### Diseño Visual Diferenciado

#### En Páginas de Meetups (Rectangulares)
```css
.speaker-photo img {
  width: 160px;
  height: 160px;
  /* SIN border-radius - rectangulares */
  border: 2px solid var(--md-default-fg-color--lightest);
}
```

#### En Páginas de Ponentes/Voluntarios (Circulares)
```css
.volunteer-avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%; /* Circulares */
  border: 3px solid var(--md-primary-fg-color--light);
}
```

## Layout y Responsive

### Breakpoint Principal

**Mobile**: `< 768px`
**Desktop**: `≥ 768px`

```css
@media (max-width: 768px) {
  .participation-grid,
  .year-cards {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .community-links {
    justify-content: center;
    gap: 0.75rem;
  }

  .volunteer-card .card-header {
    grid-template-columns: 1fr;
    text-align: center;
    gap: 1.5rem;
  }

  .speaker-photo img {
    width: 120px;
    height: 120px;
  }
}
```

### Patrones de Grid

#### Auto-fit con Mínimo
```css
grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
```

#### Grillas Específicas
```css
/* Participación */
.participation-grid {
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}

/* Enlaces de comunidad */
.community-links {
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}

/* Comunidades aliadas */
.communities-grid {
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
}
```

## Buenas Prácticas

### ✅ Variables-First Approach

```css
/* ✅ Correcto */
.nuevo-componente {
  background: var(--python-green);
  color: var(--badge-technical);
  border-radius: var(--card-radius);
  transition: var(--transition-base);
  margin: var(--space-md);
}

/* ❌ Incorrecto */
.nuevo-componente {
  background: #4CAF50;
  color: #37474F;
  border-radius: 0.75rem;
  transition: all 0.3s ease;
  margin: 1.5rem;
}
```

### ✅ Sistema Unificado

```css
/* ✅ Correcto - Usar clases existentes */
<div class="volunteer-card">
  <div class="card-header">
    <!-- estructura unificada -->
  </div>
</div>

/* ❌ Incorrecto - Crear nuevas estructuras */
<div class="speaker-profile-card">
  <!-- estructura diferente -->
</div>
```

### ✅ Mobile-First

```css
/* ✅ Correcto - Base móvil, luego desktop */
.component {
  font-size: 1rem;
  padding: 1rem;
}

@media (min-width: 768px) {
  .component {
    font-size: 1.2rem;
    padding: 2rem;
  }
}
```

### ✅ Nomenclatura Consistente

```css
/* ✅ Correcto */
.volunteer-card           /* Componente principal */
.volunteer-card .card-header  /* Elemento del componente */
.volunteer-card .badge.technical  /* Modificador */

/* ❌ Incorrecto */
.volunteerCard
.card_header
.technicalBadge
```

### ❌ Qué NO hacer

1. **Estilos inline** - Usar siempre classes CSS
2. **Colores hardcoded** - Usar variables CSS
3. **`!important`** - Usar especificidad apropiada
4. **Múltiples breakpoints** - Mantener único en 768px
5. **Componentes duplicados** - Reutilizar sistema unificado

## Troubleshooting

### Problemas Comunes

#### 1. Estilos No Aplicados

**Verificar**:
- ¿Está incluido `custom.css` en `mkdocs.yml`?
- ¿La especificidad CSS es suficiente?
- ¿Hay conflictos con Material Design?

**Solución**:
```css
/* Aumentar especificidad sin !important */
.md-content .volunteer-card {
  /* estilos */
}
```

#### 2. Modo Oscuro Problemático

```css
/* ❌ Problemático */
.component {
  color: #333;
  background: white;
}

/* ✅ Correcto */
.component {
  color: var(--md-default-fg-color);
  background: var(--md-default-bg-color);
}
```

#### 3. Responsive Roto

```css
/* ❌ Problemático */
.grid {
  grid-template-columns: 300px 300px 300px;
}

/* ✅ Correcto */
.grid {
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
}
```

#### 4. Variables No Definidas

**Error común**: Usar variables que no existen
```css
/* ❌ Variable inexistente */
color: var(--primary-blue);

/* ✅ Variable correcta */
color: var(--year-2024-color);
```

## Checklist para Nuevos Componentes

- [ ] ¿Usa variables CSS en lugar de valores hardcoded?
- [ ] ¿Es responsive con el breakpoint único (768px)?
- [ ] ¿Funciona en modo claro y oscuro?
- [ ] ¿Sigue las naming conventions establecidas?
- [ ] ¿Reutiliza el sistema unificado cuando es apropiado?
- [ ] ¿Tiene estados hover/focus con transiciones?
- [ ] ¿Es accesible y semánticamente correcto?
- [ ] ¿Está documentado en esta guía?

## Referencias

- [MkDocs Material Variables](https://squidfunk.github.io/mkdocs-material/customization/#additional-css)
- [CSS Variables MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)
- [FontAwesome Icons](https://fontawesome.com/icons)

---

**Última actualización**: Esta guía se mantiene sincronizada con `docs/css/custom.css` (~1466 líneas)
