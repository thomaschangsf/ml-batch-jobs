# Use slim Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first to leverage Docker caching
COPY pipeline-runtime/requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install pytest

# Copy the actual application code
COPY pipeline-runtime/ ./pipeline-runtime/

# Set environment variable for consistent logs
ENV PYTHONUNBUFFERED=1

# Default command (can be overridden)
CMD ["pytest", "pipeline-runtime/kernel/tests"]
