#!/usr/bin/env python3
"""
Script para gestionar enlaces de YouTube de los meetups
"""

# Enlaces de YouTube por meetup (formato: 'YYYYMM': 'video_id')
YOUTUBE_LINKS = {
    # 2023
    "202309": "YNcqrukgQQY",  # AWS AI + Metaprogramación
    "202310": "vhlPmOgrvUA",  # Jupyter a Web
    "202311": "GxBpandei-w",  # GitOps + Python Language
    # 2024
    "202401": "live_stream",  # Ambientes virtuales
    "202402": "live_stream",  # Interfaces gráficas
    "202403": "MMHaIrZ1ISw",  # Flask APIs
    "202404": "emJYJhFe0l8",  # Contenedores
    "202405": "acpwiu_sfjk",  # Pydantic
    "202406": "BmSI2IgHG_c",  # Regresión Lineal
    "202407": "o9AGel1P_qU",  # Python sin GIL + ETLs
    "202408": "live_stream",  # Protocolos + Open Source
    "202409": "live_stream",  # Fonética + Rich/Textual
    "202410": "live_stream",  # Contribuir a Open Source
    "202411": "live_stream",  # Anti-patrones + ChatGPT
    # 2025
    "202501": "live_stream",  # LibreOffice + PCI DSS
    "202502": "live_stream",  # Embeddings + Advent of Code
    "202503": "live_stream",  # Agentes IA + PySide6
    "202504": "live_stream",  # Kubernetes + AI
    "202505": "live_stream",  # PyPI
    "202506": "live_stream",  # Software libre
}


def get_youtube_embed_url(meetup_id):
    """Obtiene la URL de embed de YouTube para un meetup"""
    video_id = YOUTUBE_LINKS.get(meetup_id, "live_stream")

    if video_id == "live_stream":
        # URL genérica para transmisión en vivo
        return (
            "https://www.youtube.com/embed/live_stream?"
            "channel=UC6vX6xr1dWQF7nQq2A9d1xw"
        )
    else:
        # URL específica para video
        return f"https://www.youtube.com/embed/{video_id}"


def get_youtube_watch_url(meetup_id):
    """Obtiene la URL de YouTube para ver el video"""
    video_id = YOUTUBE_LINKS.get(meetup_id, "live_stream")

    if video_id == "live_stream":
        # URL genérica para transmisión en vivo
        return "https://www.youtube.com/@PythonMexico/streams"
    else:
        # URL específica para video
        return f"https://www.youtube.com/watch?v={video_id}"


def update_meetup_youtube_links():
    """Actualiza los enlaces de YouTube en los archivos de meetups"""

    # Lista de archivos a actualizar
    meetup_files = [
        # 2023
        ("docs/meetups/2023/202309-septiembre.md", "202309"),
        ("docs/meetups/2023/202310-octubre.md", "202310"),
        ("docs/meetups/2023/202311-noviembre.md", "202311"),
        # 2024
        ("docs/meetups/2024/202401-enero.md", "202401"),
        ("docs/meetups/2024/202402-febrero.md", "202402"),
        ("docs/meetups/2024/202403-marzo.md", "202403"),
        ("docs/meetups/2024/202404-abril.md", "202404"),
        ("docs/meetups/2024/202405-mayo.md", "202405"),
        ("docs/meetups/2024/202406-junio.md", "202406"),
        ("docs/meetups/2024/202407-julio.md", "202407"),
        ("docs/meetups/2024/202408-agosto.md", "202408"),
        ("docs/meetups/2024/202409-septiembre.md", "202409"),
        ("docs/meetups/2024/202410-octubre.md", "202410"),
        ("docs/meetups/2024/202411-noviembre.md", "202411"),
        # 2025
        ("docs/meetups/2025/202501-enero.md", "202501"),
        ("docs/meetups/2025/202502-febrero.md", "202502"),
        ("docs/meetups/2025/202503-marzo.md", "202503"),
        ("docs/meetups/2025/202504-abril.md", "202504"),
        ("docs/meetups/2025/202505-mayo.md", "202505"),
        ("docs/meetups/2025/202506-junio.md", "202506"),
    ]

    for file_path, meetup_id in meetup_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Obtener URLs
            embed_url = get_youtube_embed_url(meetup_id)
            watch_url = get_youtube_watch_url(meetup_id)

            # Reemplazar URLs en el contenido
            # Buscar y reemplazar la URL de embed
            old_embed_pattern = (
                r"https://www.youtube.com/embed/live_stream?"
                r"channel=UC6vX6xr1dWQF7nQq2A9d1xw"
            )
            new_embed_url = embed_url

            content = content.replace(old_embed_pattern, new_embed_url)

            # Buscar y reemplazar la URL de YouTube Live
            old_watch_pattern = r"https://www.youtube.com/@PythonMexico/streams"
            new_watch_url = watch_url

            content = content.replace(old_watch_pattern, new_watch_url)

            # Escribir el archivo actualizado
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"Actualizado: {file_path}")

        except FileNotFoundError:
            print(f"Archivo no encontrado: {file_path}")
        except Exception as e:
            print(f"Error actualizando {file_path}: {e}")


if __name__ == "__main__":
    print("Actualizando enlaces de YouTube en los meetups...")
    update_meetup_youtube_links()
    print("¡Enlaces actualizados!")
