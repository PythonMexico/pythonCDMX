# Guía de Estilos - Python CDMX

Esta guía documenta el sistema de diseño y estilos CSS del sitio web de Python CDMX, construido con **MkDocs Material** y **Material Design**.

## Tabla de Contenidos

- [Filosofía de Diseño](#filosofía-de-diseño)
- [Sistema de Variables](#sistema-de-variables)
- [Componentes](#componentes)
- [Layout y Grid](#layout-y-grid)
- [Buenas Prácticas](#buenas-prácticas)
- [Ejemplos de Código](#ejemplos-de-código)
- [Troubleshooting](#troubleshooting)

## Filosofía de Diseño

### Principios Fundamentales

1. **Variables First** - Todo color, espaciado y medida debe usar variables CSS
2. **Mobile First** - Diseño responsive que prioriza la experiencia móvil
3. **Consistencia** - Reutilizar componentes y patrones establecidos
4. **Accesibilidad** - Contraste adecuado y navegación clara
5. **Simplicidad** - Evitar complejidad innecesaria en CSS

### Paleta de Colores

**Verde Python** es nuestro color primario, establecido en `mkdocs.yml`:
```yaml
palette:
  - scheme: default
    primary: green
    accent: green
  - scheme: slate
    primary: green
    accent: green
```

## Sistema de Variables

### Variables Principales

```css
:root {
  /* Colores base */
  --python-green: #4CAF50;
  --python-green-dark: #45a049;
  --text-light: #ffffff;

  /* Espaciado estándar */
  --space-xs: 0.5rem;
  --space-sm: 1rem;
  --space-md: 1.5rem;
  --space-lg: 2rem;
  --space-xl: 3rem;

  /* Transiciones */
  --transition-fast: 0.2s ease;
  --transition-normal: 0.3s ease;

  /* Breakpoints */
  --mobile-breakpoint: 768px;
}
```

### Colores de Plataformas Sociales

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

## Componentes

### Sistema de Botones

#### `.btn-primary` - Botón Principal
```css
.btn-primary {
  background-color: var(--python-green);
  color: var(--text-light);
  padding: var(--space-sm) var(--space-md);
  border-radius: 0.5rem;
  transition: var(--transition-normal);
}
```

**Uso:**
```html
<a href="/meetups/" class="btn-primary">Ver Todos los Meetups</a>
```

#### `.btn` - Botón Secundario
```css
.btn {
  background-color: transparent;
  border: 2px solid var(--python-green);
  color: var(--python-green);
}
```

#### `.btn-nav` - Botón de Navegación
```css
.btn-nav {
  background-color: transparent;
  border: 1px solid #555;
  color: #888;
  font-size: 0.9rem;
}
```

### Enlaces de Comunidad

#### Estructura HTML
```html
<div class="community-links">
  <a href="https://t.me/PythonCDMX" class="community-link telegram">
    <i class="fab fa-telegram"></i>
    <span>Telegram</span>
  </a>
  <!-- Más enlaces... -->
</div>
```

#### CSS con Colores por Plataforma
```css
.community-links {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--space-sm);
}

.community-link.telegram:hover {
  background-color: var(--telegram-color);
  color: white;
}
```

### Tarjetas de Participación

#### Estructura HTML
```html
<div class="participation-cards">
  <div class="participation-card">
    <div class="card-icon">
      <i class="fas fa-microphone-alt"></i>
    </div>
    <h3>Propón una Charla</h3>
    <p>Comparte tu conocimiento...</p>
  </div>
</div>
```

#### CSS Grid Responsive
```css
.participation-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(18.75rem, 1fr));
  gap: var(--space-md);
  margin: var(--space-lg) 0;
}

.participation-card {
  text-align: center;
  padding: var(--space-lg);
  border-radius: 0.5rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
```

### Lema de la Comunidad

```css
.community-motto {
  background-color: var(--md-default-bg-color);
  border-left: 4px solid var(--python-green);
  border-radius: 0.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  font-size: 1.1rem;
  font-style: italic;
  margin: var(--space-sm) 0;
  padding: var(--space-md);
  position: relative;
  text-align: center;
}
```

## Layout y Grid

### Breakpoint Principal

**Mobile**: `< 768px`
**Desktop**: `≥ 768px`

```css
@media (max-width: 767px) {
  .hero-logo {
    max-width: 5rem;
  }

  .participation-cards {
    grid-template-columns: 1fr;
  }

  .community-links {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

### Grid Patterns

#### Auto-fit con Mínimo
```css
grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
```

#### Dos Columnas en Móvil
```css
grid-template-columns: repeat(2, 1fr);
```

#### Altura Uniforme
```css
.community-link {
  height: 60px;
  display: flex;
  align-items: center;
}
```

## Buenas Prácticas

### ✅ Qué SÍ hacer

1. **Usar variables CSS**
   ```css
   /* ✅ Correcto */
   color: var(--python-green);
   margin: var(--space-md);

   /* ❌ Incorrecto */
   color: #4CAF50;
   margin: 1.5rem;
   ```

2. **Mobile First**
   ```css
   /* ✅ Correcto - Base móvil, luego desktop */
   .component {
     font-size: 1rem;
   }

   @media (min-width: 768px) {
     .component {
       font-size: 1.2rem;
     }
   }
   ```

3. **Nomenclatura BEM**
   ```css
   /* ✅ Correcto */
   .community-link
   .community-link--active
   .community-link__icon
   ```

4. **Reutilizar componentes**
   ```html
   <!-- ✅ Correcto -->
   <a href="/link" class="btn-primary">Botón</a>

   <!-- ❌ Incorrecto -->
   <a href="/link" style="background: green;">Botón</a>
   ```

### ❌ Qué NO hacer

1. **Estilos inline**
2. **Hardcodear medidas**
3. **Colores sin variables**
4. **CSS específico por página**
5. **Romper responsive**

### Naming Conventions

#### Clases de Componentes
- `.btn-*` - Sistema de botones
- `.community-*` - Enlaces de comunidad
- `.participation-*` - Tarjetas de participación
- `.hero-*` - Elementos del hero
- `.upcoming-*` - Eventos próximos

#### Variables CSS
- `--python-*` - Colores de la marca
- `--space-*` - Espaciado (xs, sm, md, lg, xl)
- `--*-color` - Colores de plataformas
- `--transition-*` - Animaciones

## Ejemplos de Código

### Nuevo Componente de Botón

```css
.btn-warning {
  background-color: #ff9800;
  border: none;
  border-radius: 0.5rem;
  color: var(--text-light);
  padding: var(--space-sm) var(--space-md);
  transition: var(--transition-normal);
}

.btn-warning:hover {
  background-color: #f57c00;
  transform: translateY(-2px);
}
```

### Nueva Tarjeta de Contenido

```css
.content-card {
  background-color: var(--md-default-bg-color);
  border-radius: 0.5rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  padding: var(--space-lg);
  transition: var(--transition-normal);
}

.content-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  transform: translateY(-2px);
}

@media (max-width: 767px) {
  .content-card {
    padding: var(--space-md);
  }
}
```

### Grid de Eventos

```css
.events-grid {
  display: grid;
  gap: var(--space-md);
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  margin: var(--space-lg) 0;
}

@media (max-width: 767px) {
  .events-grid {
    grid-template-columns: 1fr;
    gap: var(--space-sm);
  }
}
```

## Troubleshooting

### Problemas Comunes

#### 1. Contraste en Modo Oscuro

**Problema**: Texto no legible en modo oscuro
```css
/* ❌ Problemático */
.component {
  color: #333;
}
```

**Solución**: Usar variables de MkDocs Material
```css
/* ✅ Correcto */
.component {
  color: var(--md-default-fg-color);
}
```

#### 2. Responsive Roto

**Problema**: Grid no responsivo
```css
/* ❌ Problemático */
.grid {
  grid-template-columns: 1fr 1fr 1fr;
}
```

**Solución**: Auto-fit con mínimo
```css
/* ✅ Correcto */
.grid {
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}
```

#### 3. Estilos No Aplicados

**Verificar**:
1. ¿Está incluido `custom.css` en `mkdocs.yml`?
2. ¿La especificidad CSS es suficiente?
3. ¿Hay conflictos con Material Design?

**Solución de especificidad**:
```css
/* Si no se aplica */
.md-content .mi-componente {
  /* estilos */
}
```

#### 4. Animaciones Lentas

**Problema**: Transiciones muy largas
```css
/* ❌ Lento */
transition: all 1s ease;
```

**Solución**: Usar variables de transición
```css
/* ✅ Correcto */
transition: var(--transition-normal);
```

## Mantenimiento

### Checklist de Nuevos Componentes

- [ ] ¿Usa variables CSS?
- [ ] ¿Es responsive?
- [ ] ¿Funciona en modo claro y oscuro?
- [ ] ¿Sigue naming conventions?
- [ ] ¿Está documentado aquí?
- [ ] ¿Tiene estados hover/focus?
- [ ] ¿Es accesible?

### Actualizar Variables

1. Definir en `:root`
2. Usar en componentes
3. Actualizar esta guía
4. Probar en ambos modos

### Testing

```bash
# Servidor local
mkdocs serve

# Verificar en:
# - http://localhost:8000 (modo claro)
# - Alternar a modo oscuro
# - Responsive en DevTools
# - Todas las páginas principales
```

---

**Última actualización**: Esta guía se mantiene sincronizada con `docs/css/custom.css`
