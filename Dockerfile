FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        default-libmysqlclient-dev \
        build-essential \
        pkg-config \
        dos2unix \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create directories for static and media files
RUN mkdir -p /app/static /app/media

# Create a non-root user
RUN useradd -m myuser

# Copy entrypoint first and set permissions
COPY entrypoint.sh .
RUN dos2unix entrypoint.sh && \
    chmod +x entrypoint.sh

# Copy project files
COPY . .
RUN chown -R myuser:myuser /app

USER myuser