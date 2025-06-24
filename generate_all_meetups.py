#!/usr/bin/env python3
import glob
import json
import os

from jinja2 import Environment, FileSystemLoader


def create_meetup_file(json_file):
    """Crea un archivo markdown para un meetup desde JSON usando templates Jinja2."""

    # Configurar Jinja2
    env = Environment(loader=FileSystemLoader("templates"))

    # Cargar datos
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Crear directorio
    year = data["id"][:4]
    output_dir = f"docs/meetups/{year}"
    os.makedirs(output_dir, exist_ok=True)

    # Generar archivo
    filename = f"{data['id']}.md"
    output_path = os.path.join(output_dir, filename)

    # Determinar qué template usar basado en el número de charlas
    if len(data.get("talks", [])) > 1:
        template = env.get_template("meetup-template-multiple-talks.md.j2")
    else:
        template = env.get_template("meetup-template.md.j2")

    # Preparar datos para el template
    template_data = {
        "event_title": data["event_title"],
        "event_subtitle": data["event_subtitle"],
        "event_date": data["event_date"],
        "event_time": data["event_time"],
        "event_location": data["event_location"],
        "event_rsvp_link": data.get("event_rsvp_link", "#"),
        "event_banner_image": data.get(
            "event_banner_image", "/assets/images/default-banner.jpg"
        ),
        "event_month_year": f"{data['event_date'].split()[1]} {data['event_date'].split()[-1]}",
        "tags": data["tags"],
        "last_update": data.get("last_update", "Generado automáticamente"),
    }

    # Agregar datos específicos según el tipo de template
    if len(data.get("talks", [])) > 1:
        template_data["talks"] = data["talks"]
    else:
        # Para template de una sola charla
        if data.get("talks"):
            talk = data["talks"][0]
            template_data["talk"] = talk
            template_data["speaker"] = talk.get("speaker", {})
        else:
            # Fallback si no hay charlas definidas
            template_data["talk"] = {
                "title": data["event_title"],
                "description": data["event_subtitle"],
                "conclusion": "Más detalles próximamente...",
                "tech_stack": [],
            }
            template_data["speaker"] = {
                "name": "Ponente por confirmar",
                "title": "TBD",
                "bio": "Información del ponente próximamente...",
                "photo": "/assets/images/default-speaker.jpg",
            }

    # Agregar video si existe
    if data.get("video"):
        template_data["video"] = data["video"]

    # Renderizar template
    content = template.render(**template_data)

    # Escribir archivo
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ {output_path}")
    return output_path


def main():
    """Genera todos los meetups faltantes."""
    print("🚀 Generando meetups faltantes...")

    # Buscar archivos JSON en la carpeta metadata_json
    json_files = (
        glob.glob("metadata_json/meetup-2023*.json")
        + glob.glob("metadata_json/meetup-2024*.json")
        + glob.glob("metadata_json/meetup-2025*.json")
    )
    json_files.sort()

    print(f"📁 Procesando {len(json_files)} archivos...")

    count = 0
    for json_file in json_files:
        try:
            create_meetup_file(json_file)
            count += 1
        except Exception as e:
            print(f"❌ Error en {json_file}: {e}")

    print(f"\n🎉 Se generaron {count} archivos markdown!")


if __name__ == "__main__":
    main()
