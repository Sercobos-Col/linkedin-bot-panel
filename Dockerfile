# Usamos una imagen base con Python
FROM python:3.10-slim

# Instalamos las dependencias necesarias
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gnupg2 \
    unzip \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    libx11-xcb1 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

# Instalar Chromium
RUN wget -q -O - https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb > /tmp/chrome.deb && \
    dpkg -i /tmp/chrome.deb && \
    apt-get -y install -f

# Instalar Playwright y dependencias
RUN pip install playwright
RUN playwright install

# Crear un directorio para la app
WORKDIR /app
COPY . /app

# Instalar dependencias de la app
RUN pip install -r requirements.txt

# Exponer el puerto que usará Streamlit
EXPOSE 8501

# Ejecutar la aplicación
CMD ["streamlit", "run", "app.py"]
