# Componentes Comunes para Meetups

Este directorio contiene componentes reutilizables para las páginas de meetups.

## 📁 Archivos disponibles

### `networking.md`
Sección de networking que se incluye al final de cada meetup.

### `community-links.md`
Enlaces a las redes sociales y plataformas de la comunidad.

### `footer.md`
Footer común con información de última actualización.

## 🎯 Beneficios

- **Mantenimiento centralizado**: Cambios en un solo lugar se reflejan en todos los meetups
- **Consistencia**: Todos los eventos tienen el mismo estilo y estructura
- **Reutilización**: No hay que duplicar código
- **Facilidad de actualización**: Modificar enlaces o estilos es más sencillo

## 📝 Cómo usar los componentes

Actualmente los componentes están embebidos directamente en los archivos de meetups para evitar problemas con el plugin de snippets.

### Ejemplo de uso:

```markdown
## Contenido específico del meetup...

<!-- Sección de networking embebida -->
<div class="networking-section">
  <h3>💬 ¡Conecta con la comunidad!</h3>
  <p>
    Después de la charla habrá un tiempo de networking donde podrás platicar con programadores de diferentes niveles e intereses.
  </p>
</div>

<!-- Enlaces de la comunidad embebidos -->
<div class="community-links">
  <a href="https://t.me/PythonCDMX">
    📱 Telegram
  </a>
  <!-- Más enlaces... -->
</div>
```

## 🔧 Modificaciones

Si necesitas modificar algún componente:

1. Edita el archivo correspondiente en este directorio
2. Copia el contenido actualizado a los meetups que lo usen
3. Mantén la consistencia visual y de estilo

## 🗂️ Estructura de directorios

```
docs/
├── components/
│   ├── networking.md
│   ├── community-links.md
│   ├── footer.md
│   └── README.md
├── meetups/
│   ├── 2025/
│   │   ├── 202506-junio.md
│   │   └── ...
│   └── ...
└── ...
```

## ⚠️ Nota importante

Los componentes están embebidos directamente en los archivos de meetups para evitar problemas con el plugin `pymdownx.snippets`. Esto asegura que el sitio funcione correctamente sin errores de compilación.
