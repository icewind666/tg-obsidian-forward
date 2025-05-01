# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    TZ=UTC

# Create a directory for the bot
WORKDIR /usr/src/app

# Install system dependencies including ffmpeg and curl
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    curl \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a directory for models and download Whisper model
RUN mkdir -p /models && \
    cd /models && \
    curl -O https://openaipublic.blob.core.windows.net/whisper/models/medium.pt

# Copy requirements first to leverage Docker cache
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create necessary directories
RUN mkdir -p /usr/src/app/img

# Set proper permissions
RUN chmod +x /usr/src/app/tg-obsidian-forward-bot.py

# Define the command to run the bot
CMD ["python", "./tg-obsidian-forward-bot.py"]

# Install additional Python packages (Ensure that the necessary packages are included in requirements.txt)
RUN pip install aiogram beautifulsoup4 aiohttp torch torchvision torchaudio lxml ollama