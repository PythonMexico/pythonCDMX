# Dockerfile para Python CDMX Charlas
# Basado en Python 3.11 slim para optimizar el tamaño

FROM python:3.11-slim

# Establecer variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Instalar dependencias del sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
        curl \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Crear usuario no-root para seguridad
RUN groupadd -r mkdocs && useradd -r -g mkdocs mkdocs

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente
COPY . .

# Cambiar propietario de archivos
RUN chown -R mkdocs:mkdocs /app

# Cambiar a usuario no-root
USER mkdocs

# Exponer puerto
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/ || exit 1

# Comando por defecto
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]

# Etiquetas de metadatos
LABEL maintainer="Python CDMX <info@pythoncdmx.org>" \
      description="Sitio web oficial de Python CDMX Charlas" \
      version="1.0.0" \
      org.opencontainers.image.source="https://github.com/PythonMexico/python-cdmx-page"
