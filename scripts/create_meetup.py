#!/usr/bin/env python3
"""
Script para crear nuevos meetups usando el template
Uso: python scripts/create_meetup.py
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path


def get_template_content():
    """Lee el contenido del template"""
    template_path = Path("docs/templates/meetup-template.md")
    if not template_path.exists():
        print(
            "❌ Error: No se encontró el template en docs/templates/meetup-template.md"
        )
        sys.exit(1)

    return template_path.read_text(encoding="utf-8")


def get_user_input():
    """Obtiene la información del usuario para el nuevo meetup"""
    print("🐍 Creando nuevo meetup para PythonCDMX")
    print("=" * 50)

    # Información básica del evento
    print("\n📅 INFORMACIÓN BÁSICA DEL EVENTO:")
    event_banner = input(
        "Ruta de la imagen del banner (ej: /images/meetup/202507-pythoncdmx.png): "
    ).strip()
    event_month_year = input("Mes y año del evento (ej: Julio 2025): ").strip()
    event_title = input("Título principal de la charla: ").strip()
    event_subtitle = input("Subtítulo o descripción corta: ").strip()
    event_date = input("Fecha completa (ej: Martes 15 de Julio, 2025): ").strip()
    event_time = input("Horario (ej: 18:30 - 21:00): ").strip()
    event_location = input("Lugar del evento: ").strip()
    event_rsvp = input(
        "Enlace para registro (ej: https://www.meetup.com/python-mexico/): "
    ).strip()

    # Información del ponente
    print("\n🎤 INFORMACIÓN DEL PONENTE:")
    speaker_photo = input(
        "Ruta de la foto del ponente (ej: /images/ponentes/202507-PythonCDMX-nombre.jpg): "
    ).strip()
    speaker_name = input("Nombre completo del ponente: ").strip()
    speaker_title = input("Título o cargo del ponente: ").strip()
    speaker_bio = input("Biografía del ponente: ").strip()

    # Enlaces del ponente (opcionales)
    speaker_linkedin = input(
        "Enlace a LinkedIn (opcional, Enter para omitir): "
    ).strip()
    speaker_github = input("Enlace a GitHub (opcional, Enter para omitir): ").strip()
    speaker_twitter = input("Enlace a Twitter (opcional, Enter para omitir): ").strip()

    # Información de la charla
    print("\n🎯 INFORMACIÓN DE LA CHARLA:")
    talk_title = input("Título de la charla: ").strip()
    talk_description = input("Descripción detallada de la charla: ").strip()
    talk_conclusion = input("Conclusión o cierre de la charla: ").strip()

    # Stack tecnológico (opcional)
    print("\n🔧 STACK TECNOLÓGICO (opcional):")
    tech_stack = input("¿Incluir sección de tecnologías? (s/n): ").strip().lower()
    tech_stack_items = ""
    if tech_stack == "s":
        print("Ingresa las tecnologías (una por línea, Enter vacío para terminar):")
        tech_items = []
        while True:
            tech = input("Tecnología (ej: 🐍 Python): ").strip()
            if not tech:
                break
            tech_items.append(tech)

        if tech_items:
            tech_stack_items = []
            for item in tech_items:
                tech_stack_items.append(
                    f'<div style="background: white; padding: 1rem; border-radius: 8px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">'
                )
                tech_stack_items.append(
                    f'    <h4 style="margin: 0 0 0.5rem 0; color: #007bff;">{item}</h4>'
                )
                tech_stack_items.append(
                    f'    <p style="margin: 0; font-size: 0.9rem;">Tecnología destacada</p>'
                )
                tech_stack_items.append(f"</div>")
            tech_stack_items = "\n".join(tech_stack_items)

    # Tags/Tecnologías
    print("\n🏷️ TAGS/TECNOLOGÍAS:")
    tags_input = input(
        "Tags separados por coma (ej: Python, Machine Learning, Web): "
    ).strip()
    tags = []
    if tags_input:
        tag_list = [tag.strip() for tag in tags_input.split(",")]
        colors = [
            "#007bff",
            "#28a745",
            "#ffc107",
            "#17a2b8",
            "#6f42c1",
            "#e83e8c",
            "#fd7e14",
            "#dc3545",
        ]
        for i, tag in enumerate(tag_list):
            color = colors[i % len(colors)]
            text_color = "black" if color == "#ffc107" else "white"
            tags.append(
                f'<span style="background: {color}; color: {text_color}; padding: 0.5rem 1rem; border-radius: 20px; font-weight: 600;">{tag}</span>'
            )

    tags_html = "\n".join(tags)

    # Video de YouTube (opcional)
    print("\n🎥 VIDEO DE YOUTUBE (opcional):")
    has_video = input("¿Hay video de YouTube? (s/n): ").strip().lower()
    youtube_id = ""
    youtube_url = ""
    if has_video == "s":
        youtube_url = input("URL completa del video de YouTube: ").strip()
        # Extraer ID del video
        match = re.search(
            r"(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&\n?#]+)", youtube_url
        )
        if match:
            youtube_id = match.group(1)
        else:
            print(
                "⚠️  No se pudo extraer el ID del video. Usa el formato: https://www.youtube.com/watch?v=ID"
            )
            youtube_id = input("ID del video de YouTube: ").strip()

    return {
        "EVENT_BANNER_IMAGE": event_banner,
        "EVENT_MONTH_YEAR": event_month_year,
        "EVENT_TITLE": event_title,
        "EVENT_SUBTITLE": event_subtitle,
        "EVENT_DATE": event_date,
        "EVENT_TIME": event_time,
        "EVENT_LOCATION": event_location,
        "EVENT_RSVP_LINK": event_rsvp,
        "SPEAKER_PHOTO": speaker_photo,
        "SPEAKER_NAME": speaker_name,
        "SPEAKER_TITLE": speaker_title,
        "SPEAKER_BIO": speaker_bio,
        "SPEAKER_LINKEDIN": speaker_linkedin,
        "SPEAKER_GITHUB": speaker_github,
        "SPEAKER_TWITTER": speaker_twitter,
        "TALK_TITLE": talk_title,
        "TALK_DESCRIPTION": talk_description,
        "TALK_CONCLUSION": talk_conclusion,
        "TECH_STACK_ITEMS": tech_stack_items,
        "YOUTUBE_VIDEO_ID": youtube_id,
        "YOUTUBE_VIDEO_URL": youtube_url,
        "TAGS": tags_html,
    }


def replace_variables(template_content, variables):
    """Reemplaza las variables en el template"""
    content = template_content

    # Reemplazar variables básicas
    for key, value in variables.items():
        if value:  # Solo reemplazar si hay valor
            content = content.replace(f"{{{{ {key} }}}}", value)

    # Manejar secciones condicionales
    if not variables["YOUTUBE_VIDEO_ID"]:
        # Eliminar sección de video
        content = re.sub(
            r"{{#if YOUTUBE_VIDEO_ID}}.*?{{/if}}", "", content, flags=re.DOTALL
        )

    if not variables["TECH_STACK_ITEMS"]:
        # Eliminar sección de tech stack
        content = re.sub(
            r"{{#if TECH_STACK_ITEMS}}.*?{{/if}}", "", content, flags=re.DOTALL
        )

    # Eliminar enlaces vacíos del ponente
    if not variables["SPEAKER_LINKEDIN"]:
        content = re.sub(
            r"{{#if SPEAKER_LINKEDIN}}.*?{{/if}}", "", content, flags=re.DOTALL
        )
    if not variables["SPEAKER_GITHUB"]:
        content = re.sub(
            r"{{#if SPEAKER_GITHUB}}.*?{{/if}}", "", content, flags=re.DOTALL
        )
    if not variables["SPEAKER_TWITTER"]:
        content = re.sub(
            r"{{#if SPEAKER_TWITTER}}.*?{{/if}}", "", content, flags=re.DOTALL
        )

    return content


def get_filename():
    """Genera el nombre del archivo basado en la fecha"""
    while True:
        filename = input("\n📁 Nombre del archivo (ej: 202507-julio.md): ").strip()
        if filename.endswith(".md"):
            return filename
        else:
            print("❌ El archivo debe terminar en .md")


def save_meetup(content, filename):
    """Guarda el meetup en el archivo especificado"""
    # Determinar el año del archivo
    year_match = re.search(r"(\d{4})", filename)
    if year_match:
        year = year_match.group(1)
    else:
        year = str(datetime.now().year)

    # Crear directorio si no existe
    output_dir = Path(f"docs/meetups/{year}")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Guardar archivo
    output_path = output_dir / filename
    output_path.write_text(content, encoding="utf-8")

    print(f"✅ Meetup creado exitosamente en: {output_path}")
    return output_path


def main():
    """Función principal"""
    print("🐍 Generador de Meetups PythonCDMX")
    print("=" * 40)

    try:
        # Obtener template
        template_content = get_template_content()

        # Obtener información del usuario
        variables = get_user_input()

        # Obtener nombre del archivo
        filename = get_filename()

        # Reemplazar variables
        content = replace_variables(template_content, variables)

        # Guardar archivo
        output_path = save_meetup(content, filename)

        print(f"\n🎉 ¡Meetup creado exitosamente!")
        print(f"📁 Archivo: {output_path}")
        print(f"🌐 Para verlo: mkdocs serve")
        print(f"📝 Recuerda revisar y ajustar el contenido según sea necesario")

    except KeyboardInterrupt:
        print("\n\n❌ Operación cancelada por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
