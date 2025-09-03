# Blog Media

Esta carpeta contiene las imágenes utilizadas en los artículos del blog, organizadas por artículo.

## Estructura

```
media/
├── README.md
└── PyconLatam2025/
    ├── image1.png
    ├── image2.png
    ├── ...
    └── image12.png
```

## Organización por artículo

Cada artículo del blog tiene su propia carpeta dentro de `media/` con el mismo nombre que el archivo `.md`:

- `PyconLatam2025/` - Imágenes del artículo PyCon Latam 2025
- `futuro-articulo/` - Imágenes de futuros artículos

## Proceso de extracción

Las imágenes fueron extraídas automáticamente desde el archivo `PyconLatam2025.md` y organizadas en su carpeta correspondiente.

## Agregar nuevos artículos

Para crear un nuevo artículo del blog, usa el script de configuración:

```bash
python scripts/setup_blog_article.py nombre-del-articulo
```

Este script:
- Crea el archivo `docs/blog/nombre-del-articulo.md`
- Crea la carpeta `docs/blog/media/nombre-del-articulo/`
- Agrega el artículo a la navegación en `.pages`
- Incluye plantilla básica con ejemplos

## Agregar nuevas imágenes

Para agregar nuevas imágenes al blog:

1. **Crear carpeta del artículo** (si no existe):
   ```bash
   mkdir docs/blog/media/nombre-del-articulo
   ```

2. **Colocar las imágenes** en la carpeta del artículo

3. **Referenciar en el markdown**:
   ```markdown
   ![alt text](media/nombre-del-articulo/imagen.png)
   ```

   O usar definiciones:
   ```markdown
   [nombre]: media/nombre-del-articulo/imagen.png
   ```

## Convenciones de nombres

- **Carpetas**: Mismo nombre que el archivo `.md` (sin extensión)
- **Imágenes**: Nombres descriptivos y únicos dentro de cada carpeta
- **Formatos**: PNG, JPG, GIF, SVG (preferir PNG para capturas de pantalla)
