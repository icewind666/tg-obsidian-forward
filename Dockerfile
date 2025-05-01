# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Create a directory for the bot
WORKDIR /usr/src/app

# Copy the requirements.txt file into the container
COPY requirements.txt ./

COPY structure.json ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install system dependencies including ffmpeg and curl
RUN apt-get update && apt-get install -y ffmpeg libsndfile1 curl --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a directory for models and download Whisper model
RUN mkdir -p /models && \
    cd /models && \
    curl -O https://openaipublic.blob.core.windows.net/whisper/models/medium.pt

# Copy the bot script and config file into the container
COPY tg-obsidian-forward-bot.py ./
COPY config.py ./

# Define the command to run the bot
CMD ["python", "./tg-obsidian-forward-bot.py"]

# Install additional Python packages (Ensure that the necessary packages are included in requirements.txt)
RUN pip install aiogram beautifulsoup4 aiohttp torch torchvision torchaudio lxml ollama