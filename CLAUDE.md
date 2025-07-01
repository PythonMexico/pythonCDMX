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
- **Component-based**: Clear separation of concerns
- **Heavily optimized**: Eliminated duplications, reduced code by 35%

### Component Classes

#### Core Layout
- `.hero-section` - Main landing area with logo and buttons
- `.community-motto` - Highlighted community slogan with decorative quotes
- `.participation-grid` - 2-column grid (1 on mobile) with centered 3rd card

#### Cards & Content
- `.participation-card` - Large centered icons with call-to-action buttons
- `.community-highlight` - Special highlighted sections
- `.upcoming-events` - Event highlight sections

#### Navigation & Buttons
- `.action-buttons` - Hero button containers
- `.btn`, `.btn-primary` - Standard action buttons (green)
- `.btn-nav` - Discrete navigation buttons (minimal style)
- `.quick-navigation` - End-of-page navigation grid
- `.quick-navigation-title` - Navigation section titles

#### Community Links
- `.community-links` - Social media grid with brand colors
- `.community-link` - Individual social platform buttons with hover effects
- Specific classes: `.telegram`, `.meetup`, `.youtube`, `.github`, `.instagram`, `.linkedin`

## Development Workflow

### CSS Modifications
1. **NEVER use inline styles** - Always use classes in custom.css
2. Use existing CSS variables for consistency
3. Follow the established sections in custom.css:
   - Variables CSS personalizadas
   - Sección Hero
   - Sistema de botones
   - Tarjetas y grillas
   - Enlaces de comunidad
   - Lema y navegación
   - Iconografía
   - Media queries responsivas
4. Test in both light and dark modes
5. Ensure mobile responsiveness at 768px breakpoint

### Content Updates
- Event pages: Follow existing year/month structure in `docs/meetups/`
- Images: Store in appropriate `docs/images/` subdirectories
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

### Button Types
```html
<!-- Primary action buttons -->
<a href="/path/" class="btn btn-primary">Primary Action</a>

<!-- Discrete navigation buttons -->
<a href="/path/" class="btn-nav">Navigate</a>
```

## CSS Variables Reference

### Spacing & Layout
```css
--button-radius: 3.125rem
--card-radius: 0.75rem
```

### Transitions
```css
--transition-base: all 0.3s ease
--transition-smooth: all 0.3s cubic-bezier(0.4, 0, 0.2, 1)
```

### Usage Pattern
```css
.new-component {
  background: var(--python-green);
  border-radius: var(--card-radius);
  transition: var(--transition-base);
  color: var(--python-white);
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
- CSS file currently ~450 lines (optimized from 692 lines)
- All social media colors centralized in variables
- Unified button system with three variants (primary, standard, navigation)
- Single responsive breakpoint for consistency
- Dark/light mode handled automatically by MkDocs Material variables
- Community links use brand-specific colors with smooth hover transitions
- Participation cards use large centered icons for modern appearance

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

### Integration Points
- **MkDocs Material**: Uses `extra_css` in mkdocs.yml to load custom.css
- **FontAwesome**: Loaded via CDN import in CSS file
- **Component System**: Uses `--8<--` syntax for markdown includes
- **Color System**: Inherits from mkdocs.yml palette configuration

## Recent Major Updates
- Complete CSS optimization (35% code reduction)
- New community motto component with decorative quotes
- Modernized participation cards with centered icons
- Added discrete navigation button system
- Centralized all social media brand colors
- Consolidated media queries into single responsive section
- Eliminated unused gradients and duplicate code
- Added quick navigation component for page endings

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
6. **Attach this file to Claude** - Use this memory for consistency and guidance

## Project Continuation Checklist
- [ ] CLAUDE.md file read and understood
- [ ] Current project state reviewed
- [ ] Testing environment set up (light/dark mode, mobile/desktop)
- [ ] Existing component patterns studied
- [ ] CSS variable system understood
- [ ] MkDocs Material integration grasped
