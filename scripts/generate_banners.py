#!/usr/bin/env python3
"""
Script para generar banners de meetups de Python CDMX
Usa los colores de la marca: #269f46 (verde), #000000 (negro), #e32f42 (rojo)
"""

import os
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

# Colores de la marca Python CDMX
BRAND_COLORS = {"green": "#269f46", "black": "#000000", "red": "#e32f42"}


def create_meetup_banner(year, month, title, output_path):
    """Crea un banner para un meetup específico"""

    # Dimensiones del banner (16:9 ratio)
    width, height = 1200, 675

    # Crear imagen base
    img = Image.new("RGB", (width, height), BRAND_COLORS["black"])
    draw = ImageDraw.Draw(img)

    # Intentar cargar una fuente (usar fuente por defecto si no está disponible)
    try:
        # Intentar cargar fuentes del sistema
        title_font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48
        )
        subtitle_font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32
        )
        date_font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24
        )
    except:
        # Usar fuente por defecto
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        date_font = ImageFont.load_default()

    # Dibujar elementos del banner

    # Fondo con gradiente sutil
    for y in range(height):
        alpha = int(255 * (1 - y / height * 0.3))
        color = (38, 159, 70, alpha)  # Verde con transparencia
        draw.line([(0, y), (width, y)], fill=color)

    # Línea decorativa superior
    draw.rectangle([0, 0, width, 8], fill=BRAND_COLORS["red"])

    # Logo Python (círculo simple)
    logo_center = (100, height // 2)
    logo_radius = 60
    draw.ellipse(
        [
            logo_center[0] - logo_radius,
            logo_center[1] - logo_radius,
            logo_center[0] + logo_radius,
            logo_center[1] + logo_radius,
        ],
        fill=BRAND_COLORS["green"],
    )

    # Texto "Python" en el logo
    draw.text(
        (logo_center[0] - 30, logo_center[1] - 10),
        "Python",
        fill=BRAND_COLORS["black"],
        font=subtitle_font,
    )

    # Título del meetup
    title_x = 200
    title_y = height // 2 - 80

    # Ajustar título si es muy largo
    if len(title) > 40:
        words = title.split()
        lines = []
        current_line = ""
        for word in words:
            if len(current_line + " " + word) < 40:
                current_line += " " + word if current_line else word
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)

        for i, line in enumerate(lines):
            draw.text(
                (title_x, title_y + i * 60),
                line.strip(),
                fill=BRAND_COLORS["green"],
                font=title_font,
            )
    else:
        draw.text(
            (title_x, title_y), title, fill=BRAND_COLORS["green"], font=title_font
        )

    # Subtítulo
    subtitle = f"Python CDMX Meetup"
    draw.text(
        (title_x, title_y + 120), subtitle, fill=BRAND_COLORS["red"], font=subtitle_font
    )

    # Fecha
    month_names = {
        "01": "Enero",
        "02": "Febrero",
        "03": "Marzo",
        "04": "Abril",
        "05": "Mayo",
        "06": "Junio",
        "07": "Julio",
        "08": "Agosto",
        "09": "Septiembre",
        "10": "Octubre",
        "11": "Noviembre",
        "12": "Diciembre",
    }

    date_text = f"{month_names.get(month, month)} {year}"
    draw.text((title_x, title_y + 180), date_text, fill="white", font=date_font)

    # Información adicional
    info_text = "Wizeline México • 18:30"
    draw.text((title_x, title_y + 220), info_text, fill="white", font=date_font)

    # Guardar imagen
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"Banner creado: {output_path}")


def generate_all_banners():
    """Genera banners para todos los meetups"""

    # Meetups 2023
    meetups_2023 = [
        ("09", "Utilizando Servicios AI de AWS y Metaprogramación en Python"),
        ("10", "¡De Jupyter a Web en Minutos!"),
        ("11", "GitOps 101 / Python: La Forja de un Lenguaje"),
    ]

    # Meetups 2024
    meetups_2024 = [
        ("01", "Ambientes virtuales con venv, pyenv y poetry"),
        ("02", "Del Código al Clic: Transforma Ideas en Interfaces"),
        ("03", "Desarrollo de API REST con FLASK"),
        ("04", "Desarrollo en Python usando Contenedores"),
        ("05", "Pydantic: Validaciones de datos con Type Hints"),
        ("06", "Matemáticas y Python: Ciencia Detrás de la Regresión Lineal"),
        ("07", "¡Doble Charla! Python sin GIL / Esquemas ETL"),
        ("08", "Protocolos en Python/Convertirse en Contribuidor Open Source"),
        ("09", "Representaciones Fonéticas / Rich & Textual"),
        ("10", "Una ida y una vuelta. Cómo iniciar en el opensource"),
        ("11", "Evita Anti-patrones en python / ¿Qué y por qué ChatGPT?"),
    ]

    # Meetups 2025
    meetups_2025 = [
        ("01", "Crea extensiones para LibreOffice / PCI DSS en Python"),
        ("02", "Embeddings / Advent of Code"),
        ("03", "Agentes de IA / Interfases gráficas con PySide6"),
        ("04", "Kubernetes y IA"),
        ("05", "Publicando un paquete en PyPI"),
        ("06", "Usando Python y software libre"),
    ]

    # Generar banners para 2023
    for month, title in meetups_2023:
        output_path = f"docs/images/meetup/2023{month}-pythoncdmx.png"
        create_meetup_banner("2023", month, title, output_path)

    # Generar banners para 2024
    for month, title in meetups_2024:
        output_path = f"docs/images/meetup/2024{month}-pythoncdmx.png"
        create_meetup_banner("2024", month, title, output_path)

    # Generar banners para 2025
    for month, title in meetups_2025:
        output_path = f"docs/images/meetup/2025{month}-pythoncdmx.png"
        create_meetup_banner("2025", month, title, output_path)


if __name__ == "__main__":
    print("Generando banners para todos los meetups...")
    generate_all_banners()
    print("¡Banners generados exitosamente!")
