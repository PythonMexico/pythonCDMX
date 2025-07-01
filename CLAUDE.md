# Python CDMX Project Memory

> **For New Developers**: This file contains all the essential information needed to continue developing this project using Claude AI. Read this completely before making any changes.

## Project Overview
This is the Python CDMX community website built with MkDocs Material. The site showcases meetups, community participation, and Python-related content for Mexico City's Python community with a modern Material Design approach.

**Community Motto**: *"Vine por el código, me quedé por la comunidad"* - This phrase is central to the community and prominently displayed on the homepage.

## Architecture & Technology Stack
- **Framework**: MkDocs Material
- **Styling**: Optimized custom CSS with Material Design principles
- **Content**: Markdown files with reusable HTML components
- **Deployment**: Static site generation
- **Content Management**: Manual markdown editing + automated scripts
- **Icons**: FontAwesome 6.4.0 via CDN

## File Structure & Organization
- `docs/` - All content and assets
- `docs/css/custom.css` - Main styling file (~450 lines, heavily optimized)
- `docs/index.md` - Homepage with hero section, motto, and participation cards
- `docs/components/` - Reusable markdown components
  - `community-links.md` - Social media links with brand colors
  - `quick-navigation.md` - Page navigation cards system
- `docs/meetups/` - Event documentation organized by year
- `docs/comunidad/` - Community pages (volunteers, speakers, etc.)
  - `ponentes.md` - **UPDATED**: Unified card system, alphabetical order, no tabs
  - `voluntarios.md` - Modern volunteer cards with TOC navigation
- `scripts/` - Python automation scripts for content generation

## Design System & CSS Guidelines

### Color Palette
```css
/* Primary Colors */
--python-green: #4CAF50
--python-green-dark: #45a049
--python-white: #ffffff

/* Social Media Brand Colors */
--telegram-color: #0088cc
--meetup-color: #ed1c40
--youtube-color: #ff0000
--github-color: #333333
--instagram-color: #e4405f
--linkedin-color: #0077b5
```

### CSS Architecture
- **Variables-first approach**: All colors, transitions, and spacing use CSS custom properties
- **MkDocs Material integration**: Leverages native variables (`var(--md-primary-fg-color)`)
- **Responsive design**: Single breakpoint at 768px for mobile
- **Component-based**: Clear separation of concerns with dedicated sections
- **Maintainable selectors**: Uses semantic classes instead of hardcoded identifiers
- **Optimized structure**: Consolidated media queries, unified transitions
- **Heavily optimized**: Eliminated duplications, consistent variable usage

### Component Classes

#### Core Layout
- `.hero-section` - Main landing area with logo and buttons
- `.community-motto` - Highlighted community slogan with decorative quotes
- `.participation-grid` - 2-column grid (1 on mobile) with centered 3rd card

#### Cards & Content
- `.participation-card` - Large centered icons with call-to-action buttons
- `.year-card` - Annual summaries with specialized styling and hover effects
- `.stat-card` - Statistics display cards
- `.volunteer-card` - **UNIFIED SYSTEM**: Used for both volunteers AND speakers with identical structure
  - Volunteers: Focus on community contributions and organizational roles
  - Speakers: Focus on technical specialties and recent talks
- `.community-highlight` - Special highlighted sections
- `.upcoming-events` - Event highlight sections

#### Navigation & Buttons
- `.action-buttons` - Hero button containers
- `.btn`, `.btn-primary` - Standard action buttons (green)
- `.btn-nav` - Discrete navigation buttons (minimal style)
- `.btn-action` - Volunteer card action buttons (outline style)
- `.quick-navigation` - End-of-page navigation grid
- `.quick-navigation-title` - Navigation section titles

#### Community Links
- `.community-links` - Social media grid with brand colors
- `.community-link` - Individual social platform buttons with hover effects
- Specific classes: `.telegram`, `.meetup`, `.youtube`, `.github`, `.instagram`, `.linkedin`

#### Communities & Partnerships
- `.communities-grid` - **NEW**: Auto-fit responsive grid for partner communities with minmax(280px, 1fr)
- `.community-card` - **NEW**: Partner community cards with advanced hover effects
  - Sliding shine animation on hover
  - Circular images with scale transformation
  - Smooth transitions using existing CSS variables
  - Mobile-optimized responsive design
- `.community-card img` - Circular community logos (100px) with hover scale effect
- `.community-card h3` - Community names with centered alignment
- `.community-card p` - Community descriptions with proper spacing

#### Volunteer System (Optimized & Maintainable)
- `.volunteer-card` - Main volunteer profile container with grid layout
- `.volunteer-header` - **NEW**: Maintainable class for hiding TOC headers
- `.card-header` - Two-column grid: info on left, avatar/social on right
- `.card-info` - Left column with name, subtitle, and badges
- `.card-title` - Volunteer names (h3 elements within cards)
- `.card-subtitle` - Role descriptions with proper hierarchy
- `.badges-container` - Flex container for role badges
- `.badge` - Discrete role badges with semi-transparent backgrounds
  - `.badge.ambassador` - Green theme for ambassadors
  - `.badge.organizer` - Blue theme for organizers
  - `.badge.production` - Orange theme for production roles
  - `.badge.host` - Purple theme for event hosts
  - `.badge.technical` - Gray theme for technical support
  - `.badge.support` - Brown theme for general support
  - `.badge.global` - Pink theme for global representation
  - `.badge.strategic` - Indigo theme for strategic roles
- `.avatar-section` - Right column with circular avatar and social icons
- `.volunteer-avatar` - 100px circular images with hover scale effect
- `.social-icons` - Flex container for social media links
- `.social-icon` - Individual social platform buttons
- `.card-content` - Main content area with role details
- `.card-role` - Container for role title, description, and contributions
- `.role-title` - Uppercase, prominent role titles
- `.role-description` - Italic, lighter role descriptions

## Development Workflow

### CSS Modifications
1. **NEVER use inline styles** - Always use classes in custom.css
2. **NEVER use `!important`** - Use specific selectors and proper CSS architecture instead
3. Use existing CSS variables for consistency
4. Follow the established sections in custom.css (13 organized sections):
   - Variables CSS personalizadas
   - Sección Hero
   - Sistema de botones
   - Tarjetas y grillas
   - Tarjetas de voluntarios
   - **Tarjetas de comunidades aliadas** (NEW)
   - Enlaces de comunidad
   - Lema de la comunidad
   - Navegación y secciones especiales
   - Iconografía
   - Animaciones
   - Media queries responsivas
   - Utilidades y helpers
5. Test in both light and dark modes
6. Ensure mobile responsiveness at 768px breakpoint
7. **Always prefer specific selectors over `!important`** for maintainable CSS architecture

### Content Updates
- Event pages: Follow existing year/month structure in `docs/meetups/`
- Images: Store in appropriate `docs/images/` subdirectories
  - `voluntarios/` - Volunteer profile images
  - `ponentes/` - Speaker profile images (organized alphabetically)
  - `meetup/` - Event promotional images
  - `comunidades/` - Partner community logos
- Community content: Update respective pages in `docs/comunidad/`
- Components: Use `--8<-- "components/component-name.md"` for includes

### Theme Configuration
```yaml
# mkdocs.yml
palette:
  - scheme: default
    primary: green
    accent: green
  - scheme: slate
    primary: green
    accent: green
```

## Key Components & Usage

### Community Motto
```html
<div class="community-motto">
  Vine por el código, me quedé por la comunidad
</div>
```

### Participation Cards (Modern Design)
```html
<div class="participation-grid">
  <div class="participation-card">
    <h3><i class="fas fa-microphone"></i> Ser Ponente</h3>
    <p>Description text</p>
    <a href="/link/" class="btn-primary">Action Button</a>
  </div>
</div>
```

### Community Links
```html
<div class="community-links">
  <a href="#" class="community-link telegram">
    <i class="fab fa-telegram"></i> Telegram
  </a>
  <a href="#" class="community-link github">
    <i class="fab fa-github"></i> GitHub
  </a>
</div>
```

### Quick Navigation
```html
<h2 class="quick-navigation-title">
  <i class="fas fa-arrow-right"></i> Continúa Explorando
</h2>
<div class="quick-navigation">
  <a href="/meetups/2025/" class="btn-nav">
    <i class="fas fa-calendar"></i> Meetups 2025
  </a>
</div>
```

### Communities & Partnerships
```html
<div class="communities-grid">
  <div class="community-card">
    <img src="/images/comunidades/partner-logo.png" alt="Partner Community">
    <h3>Community Name</h3>
    <p>Brief description of the partner community</p>
  </div>
</div>
```

### Unified Card System (Volunteers & Speakers)
```markdown
### Person Name {.volunteer-header}

<!-- Person Name -->
<div class="volunteer-card">
  <div class="card-header">
    <div class="card-info">
      <h3 class="card-title">Person Name</h3>
      <p class="card-subtitle">Role/Company description</p>
      <div class="badges-container">
        <!-- For Volunteers -->
        <span class="badge ambassador">Embajador</span>
        <span class="badge organizer">Organizador</span>
        <!-- For Speakers -->
        <span class="badge technical">DevOps</span>
        <span class="badge development">Desarrollo</span>
      </div>
    </div>
    <div class="avatar-section">
      <!-- Volunteers: /images/voluntarios/ -->
      <!-- Speakers: /images/ponentes/ -->
      <img src="/images/ponentes/avatar.jpg" alt="Person Name" class="volunteer-avatar lazy-image" loading="lazy">
      <div class="social-icons">
        <a href="#" class="social-icon linkedin" target="_blank"><i class="fab fa-linkedin"></i></a>
        <a href="#" class="social-icon github" target="_blank"><i class="fab fa-github"></i></a>
      </div>
    </div>
  </div>
  <div class="card-content">
    <div class="card-role">
      <!-- For Volunteers -->
      <span class="role-title">COMMUNITY ROLE TITLE</span>
      <span class="role-description">Community role description</span>
      <strong>Contribuciones principales:</strong>
      <!-- For Speakers -->
      <span class="role-title">ESPECIALIDADES TÉCNICAS</span>
      <span class="role-description">Technical specialties list</span>
      <strong>Charlas recientes:</strong>
      <ul>
        <li>Content item 1</li>
        <li>Content item 2</li>
      </ul>
    </div>
  </div>
</div>
```

**Key Features:**
- `{.volunteer-header}` automatically hides the h3 but keeps TOC functionality
- **IDENTICAL STRUCTURE** for volunteers and speakers
- Two-column grid layout with responsive design
- Circular avatars with hover effects
- Discrete badges with role-specific colors
- Social icons grouped below avatar
- **Content Differentiation**:
  - Volunteers: Community contributions and organizational roles
  - Speakers: Technical specialties and recent talks

### Button Types
```html
<!-- Primary action buttons -->
<a href="/path/" class="btn btn-primary">Primary Action</a>

<!-- Discrete navigation buttons -->
<a href="/path/" class="btn-nav">Navigate</a>
```

## CSS System Reference

> **📋 Para documentación completa del sistema de diseño y CSS, ver [`STYLE_GUIDE.md`](STYLE_GUIDE.md)**

El proyecto utiliza una **arquitectura variables-first** con 18+ variables CSS centralizadas. Para información completa sobre:

- 🎨 **Variables CSS completas** → Ver sección "Sistema de Variables" en STYLE_GUIDE.md
- 🧩 **Componentes detallados** → Ver sección "Componentes" en STYLE_GUIDE.md
- 🏗️ **Sistema unificado de tarjetas** → Ver sección dedicada en STYLE_GUIDE.md
- 📱 **Layout responsive** → Ver sección "Layout y Responsive" en STYLE_GUIDE.md
- ⚡ **Buenas prácticas** → Ver sección completa en STYLE_GUIDE.md

### Variables esenciales para IA:

```css
/* Colores principales */
--python-green: #4CAF50
--python-green-dark: #45a049

/* Badges (8 tipos completos en STYLE_GUIDE.md) */
--badge-ambassador: #2E7D32
--badge-technical: #37474F

/* Transiciones estándar */
--transition-base: all 0.3s ease
--transition-smooth: all 0.3s cubic-bezier(0.4, 0, 0.2, 1)

/* Layout */
--button-radius: 3.125rem
--card-radius: 0.75rem
```

### Patrón de uso rápido:
```css
.nuevo-componente {
  background: var(--python-green);
  border-radius: var(--card-radius);
  transition: var(--transition-base);
  /* Ver STYLE_GUIDE.md para más variables */
}
```

## Best Practices

### Styling
- **Never add inline styles** to markdown/HTML
- Always use existing component classes or create new ones in custom.css
- Maintain design consistency with existing components
- Use CSS variables for all colors and measurements
- Follow the established section order in custom.css

### Content Structure
- Use semantic HTML structure
- Include proper alt text for images
- Maintain consistent tone (Spanish for main content)
- Use reusable components via includes
- Follow existing patterns for event documentation

### Performance & Optimization
- CSS heavily optimized: removed duplications, unused code eliminated
- Images optimized before adding to repository
- Use MkDocs Material features when possible
- CSS is organized for maximum maintainability

## Responsive Design
- **Primary breakpoint**: 768px
- **Mobile-first approach**: Base styles for mobile, enhanced for desktop
- **Grid systems**: Auto-adapt to smaller screens
- **Typography**: Uses clamp() for responsive scaling

## Maintenance Notes
- CSS file currently optimized and organized (~1466 lines, heavily optimized with variables)
- **COMPLETE variables-first architecture** - Zero hardcoded colors, all use CSS custom properties
- **18 CSS variables total** - Primary colors, social media, badges, years, and layout
- All social media colors centralized in variables
- **Badge system fully variables-driven** - 8 role types with centralized color management
- Unified button system with four variants (primary, standard, navigation, action)
- Single responsive breakpoint for consistency (768px)
- Dark/light mode handled automatically by MkDocs Material variables
- Community links use brand-specific colors with smooth hover transitions
- Participation cards use large centered icons for modern appearance
- Year cards with specialized styling and gradient hover effects using CSS variables
- **Unified Design System**:
  - **Meetup speaker photos**: Rectangular (160px × 160px, no border-radius)
  - **Ponentes/Volunteer avatars**: Circular (100px × 100px via `.volunteer-avatar`)
  - **Community logos**: Circular (120px × 120px with hover effects)
- **NEW**: Comprehensive volunteer system with modern grid layout
- **NEW**: Maintainable `.volunteer-header` class eliminates hardcoded names
- **NEW**: Discrete badge system with 8 role types and consistent styling
- **NEW**: Two-column responsive design with avatar/social integration
- **UPDATED**: Speaker system completely redesigned using volunteer card structure
- **UPDATED**: All speakers alphabetically organized with unified navigation
- **UPDATED**: Dedicated `/images/ponentes/` directory for speaker photos
- **UPDATED**: Simplified single-page layout (removed tab system)
- **OPTIMIZED**: All transitions use standard variables (`var(--transition-base)`, `var(--transition-smooth)`)
- Complete responsive design for all card types with mobile-first approach
- **Zero `!important` declarations** - Clean CSS architecture with proper specificity

## Critical Information for New Developers

### DO NOT MODIFY These Files (Auto-generated or Core)
- `mkdocs.yml` - Core configuration (only change colors if needed)
- Any files in `scripts/metadata_json/` - Auto-generated meetup data
- Files generated by scripts - Check with team first

### Key Design Decisions & Rationale
1. **Single CSS File**: All custom styles in `docs/css/custom.css` to maintain simplicity
2. **Variable-First Approach**: Every color, transition, and spacing uses CSS variables for easy theming
3. **Material Design Integration**: Leverages MkDocs Material variables for automatic dark/light mode
4. **Component Includes**: Reusable components in `docs/components/` for consistency
5. **Spanish Content**: Main content in Spanish as this is a Mexico City community
6. **Social Brand Colors**: Each platform uses official brand colors for recognition
7. **Mobile-First**: 768px breakpoint chosen to match modern device patterns

### Common Troubleshooting
- **Styles not applying**: Check if using CSS variables correctly
- **Dark mode issues**: Ensure using `var(--md-*)` variables instead of hardcoded colors
- **Mobile layout broken**: Verify media query is at 768px, not other breakpoints
- **Button inconsistency**: Use `.btn-primary` for actions, `.btn-nav` for navigation
- **Icon not showing**: Verify FontAwesome class name and CDN is loading

### When to Create New Components
- **Reusable elements**: If used in 2+ places, create a component
- **Complex styling**: If requires 5+ CSS rules, consider a new class
- **Brand consistency**: Always check existing patterns before creating new styles

### Unified System Best Practices (Volunteers & Speakers)
- **Always use `.volunteer-header`**: Never hardcode names in CSS selectors
- **Badge consistency**:
  - Volunteers: Use predefined badge classes (ambassador, organizer, etc.)
  - Speakers: Use technical badges (technical, development, etc.)
- **Image optimization**: All avatars should be 200x200px minimum, optimized
- **Directory structure**:
  - Volunteers: `/images/voluntarios/filename.jpg`
  - Speakers: `/images/ponentes/filename.jpg`
- **Social links**: Include LinkedIn and GitHub at minimum, add others as needed
- **Content structure**:
  - Volunteers: Use `.role-title` for community role, focus on contributions
  - Speakers: Use "ESPECIALIDADES TÉCNICAS" as role title, focus on talks and tech
- **Organization**:
  - Volunteers: Group by role/activity
  - Speakers: **MAINTAIN ALPHABETICAL ORDER**
- **Responsive design**: Test two-column layout on mobile (becomes single column)
- **TOC navigation**: Ensure all headers work with table of contents

### Integration Points
- **MkDocs Material**: Uses `extra_css` in mkdocs.yml to load custom.css
- **FontAwesome**: Loaded via CDN import in CSS file
- **Component System**: Uses `--8<--` syntax for markdown includes
- **Color System**: Inherits from mkdocs.yml palette configuration

## Recent Major Updates

### Latest CSS Optimization & Variables System (Current Session)
- **Complete Variables-First Implementation**: Full compliance with CLAUDE.md guidelines
  - **10 new CSS variables** added for badges, years, and color management
  - **Zero hardcoded colors** - All #hex values now use CSS custom properties
  - **Unified transition system** - Consistent use of `var(--transition-base)` and `var(--transition-smooth)`
  - **Badge system optimization** - All 8 badge types now use centralized color variables
- **Professional CSS Architecture**:
  ```css
  /* NEW VARIABLES ADDED */
  --badge-ambassador: #2E7D32;
  --badge-organizer: #1565C0;
  --badge-production: #E65100;
  --badge-host: #6A1B9A;
  --badge-technical: #37474F;
  --badge-support: #3E2723;
  --badge-global: #AD1457;
  --badge-strategic: #283593;
  --year-2024-color: #2196F3;
  --year-2024-hover: #1976D2;
  --year-2023-color: #FF9800;
  --year-2023-hover: #F57C00;
  ```
- **Unified Design System Maintained**:
  - **Speaker images in meetups**: Rectangular (160px × 160px) - no border-radius
  - **Speaker images in ponentes page**: Circular via `.volunteer-avatar` (100px × 100px)
  - **Volunteer avatars**: Circular via `.volunteer-avatar` (100px × 100px)
  - **Community logos**: Circular (120px × 120px) with hover scale effects
- **CSS Code Quality Enhancement**:
  - **Zero `!important` declarations** - Clean specificity hierarchy maintained
  - **Consistent variable usage** - Every color, transition, and spacing uses CSS variables
  - **Maintainable architecture** - Easy theming and future modifications
  - **Performance optimized** - Consolidated selectors and efficient CSS organization

### Previous Major Optimizations
- **CSS Architecture Overhaul**: Complete elimination of `!important` declarations (7 instances removed)
  - Migration to specific selectors and proper CSS specificity hierarchy
  - Improved maintainability through clean CSS architecture
  - Better scalability for future modifications
- **Professional CSS Structure**: Reorganized into 13 logical sections
  1. Variables CSS personalizadas
  2. Sección Hero
  3. Sistema de botones
  4. Tarjetas y grillas
  5. Tarjetas de voluntarios
  6. **Tarjetas de comunidades aliadas** (NEW)
  7. Enlaces de comunidad
  8. Lema de la comunidad
  9. Navegación y secciones especiales
  10. Iconografía
  11. Animaciones
  12. Media queries responsivas
  13. Utilidades y helpers
- **Communities & Partnerships System**: Complete implementation of partner community styles
  - `.communities-grid`: Responsive auto-fit grid with minmax(280px, 1fr)
  - `.community-card`: Advanced hover effects with sliding shine animation
  - Circular community logos with scale effects on hover
  - Mobile-optimized responsive design with proper spacing
- **Documentation Reorganization**: Professional separation of concerns
  - **README.md**: Streamlined to essential user information and quick start
  - **CONTRIBUTING.md**: Comprehensive contribution workflow and development guidelines
  - Clear separation between user documentation and contributor guidelines
- **CSS Code Quality**: Enhanced readability and organization
  - Consistent indentation and descriptive comments
  - Consolidated social media link styles
  - Removal of redundant code and unused selectors
  - Optimized specificity hierarchy without `!important`

### Previous Major Optimizations
- **Speaker System Complete Overhaul**: All 19+ ponentes converted to modern volunteer-card layout
- **Unified Design System**: Speakers now use same structure as volunteers but with speaker-specific content
- **Organized Alphabetically**: All speakers reorganized in alphabetical order for better navigation
- **Dedicated Image Structure**: New `/images/ponentes/` directory with speaker-specific photos
- **Simplified Layout**: Removed tab system (=== "Información/"Ponentes") for cleaner single-page design
- **Real Speaker Photos**: Added actual photos for multiple speakers (Carlos Caballero, Erik Rivera, etc.)
- **Volunteer System Redesign**: Complete overhaul with modern two-column layout
- **Maintainable Architecture**: New `.volunteer-header` class eliminates hardcoded name lists
- **CSS Optimization**: Consolidated variables, eliminated duplications, unified media queries
- **TOC Navigation**: Seamless integration of volunteer cards with table of contents
- **Badge System**: Comprehensive role identification with discrete, color-coded badges
- **Avatar System**: Circular images with hover effects and integrated social icons
- **Grid Layout**: Responsive design with mobile-first approach

### Foundation Updates
- Complete CSS optimization (35% code reduction)
- New community motto component with decorative quotes
- Modernized participation cards with centered icons
- Added discrete navigation button system
- Centralized all social media brand colors
- Consolidated media queries into single responsive section
- Eliminated unused gradients and duplicate code
- Added quick navigation component for page endings
- Year cards with specialized hover effects and color coding
- Complete responsive design updates for all components

## Working with Claude AI

### Using This Memory File
When starting a new conversation with Claude:
1. **Always attach this file** - It contains all project context
2. **Reference specific sections** - Point Claude to relevant parts
3. **Update this file** - Add any new components or major changes
4. **Include current state** - Attach relevant files Claude needs to see

### Effective Prompts for Claude
```
"I'm working on the Python CDMX website. I need to [specific task].
Please refer to the CLAUDE.md file for project guidelines and existing patterns."
```

### What to Include in Conversations
- This CLAUDE.md file (always)
- Current CSS file if making style changes
- Relevant markdown files if changing content
- Screenshots if debugging visual issues

### Maintaining This Documentation
- **Add new components** to the Component Classes section
- **Update CSS variables** when adding new ones
- **Document design decisions** in the Key Design Decisions section
- **Add troubleshooting tips** based on common issues encountered

## Quick Start for New Developers
1. **Read this file completely** - Understanding the architecture is crucial
2. **Test in both modes** - Always verify light and dark mode compatibility
3. **Use existing patterns** - Check similar components before creating new ones
4. **Follow CSS structure** - Add new styles in the appropriate section
5. **Test responsive** - Verify 768px breakpoint behavior
6. **Use `.volunteer-header`** - For any volunteer-related TOC headers
7. **Follow badge system** - Use predefined badge classes for volunteer roles
8. **Attach this file to Claude** - Use this memory for consistency and guidance

## Adding New Volunteers (Step-by-Step)
1. **Add volunteer image** to `docs/images/voluntarios/` (200x200px minimum)
2. **Use the unified card template** from this file
3. **Add `.volunteer-header` class** to the markdown header
4. **Choose appropriate badges** from the predefined badge system (organizer, ambassador, etc.)
5. **Focus on community contributions** in content section
6. **Test TOC navigation** to ensure proper functionality
7. **Verify responsive design** on mobile devices

## Adding New Speakers (Step-by-Step)
1. **Add speaker image** to `docs/images/ponentes/` (200x200px minimum)
2. **Use the unified card template** from this file (same as volunteers)
3. **Add `.volunteer-header` class** to the markdown header
4. **Choose technical badges** (technical, development, etc.)
5. **Focus on specialties and talks** in content section
6. **Maintain alphabetical order** in the speakers list
7. **Test TOC navigation** to ensure proper functionality
8. **Verify responsive design** on mobile devices

## Completed System Transformations

### Speaker System Overhaul (2025)
- ✅ **21+ speakers converted** to unified volunteer-card system
- ✅ **Alphabetical organization** implemented across all speakers
- ✅ **Tab system removed** for cleaner single-page layout
- ✅ **Dedicated image directory** `/images/ponentes/` created
- ✅ **Real speaker photos** added for multiple speakers
- ✅ **Identical structure** to volunteers but with speaker-specific content
- ✅ **TOC navigation** integrated for all speakers
- ✅ **Badge system** adapted for technical specialties
- ✅ **Mobile responsive** design maintained

### Key Architectural Changes
- **Unified Card System**: Both volunteers and speakers use `.volunteer-card`
- **Content Differentiation**: Same structure, different focus areas
- **Maintainable Design**: `.volunteer-header` eliminates hardcoded selectors
- **Scalable Organization**: Alphabetical for speakers, role-based for volunteers
- **Image Management**: Separate directories for logical organization

## Project Continuation Checklist
- [ ] CLAUDE.md file read and understood
- [ ] Current project state reviewed
- [ ] Testing environment set up (light/dark mode, mobile/desktop)
- [ ] Existing component patterns studied
- [ ] CSS variable system understood
- [ ] MkDocs Material integration grasped
- [ ] Speaker vs Volunteer content structure understood
- [ ] Alphabetical organization principle for speakers followed

## Documentation Structure
- **README.md**: Essential user information, quick start, and references to detailed documentation
- **CONTRIBUTING.md**: Complete contribution workflow, detailed setup instructions, and development guidelines
- **CLAUDE.md**: This file - comprehensive technical documentation for AI development
- **CHANGELOG.md**: Release notes and feature documentation following Keep a Changelog format
