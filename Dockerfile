# Image de base Ubuntu avec Python 3.10
FROM python:3.10-slim

# Empêche les prompts interactifs
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1



# Installation de FFmpeg et outils de base
RUN apt-get update && apt-get install -y \
    ffmpeg \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app/cache /app/model /app/output /app/tmp /app/scripts
# Crée le dossier de travail
WORKDIR /app

# Copie des fichiers du projet
COPY . /app

# ✅ Installation explicite de torch 2.5.1 en version CPU
RUN pip install --upgrade pip && \
    pip install torch==2.5.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cpu && \
    pip install -r requirements.txt
    
# Exposition du port Gradio
EXPOSE 7860

ENV COQUI_TOS_AGREED=1

# Lancement conditionnel via le script start.py
CMD ["python", "start.py"]
