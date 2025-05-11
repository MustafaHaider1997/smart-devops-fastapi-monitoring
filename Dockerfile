# Use ARM-compatible base Python image
FROM python:3.11-slim-bullseye

# Set working directory
WORKDIR /app

# Copy source code
COPY main.py .

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn python-dotenv prometheus_fastapi_instrumentator

# Expose port FastAPI runs on
EXPOSE 8000

# Start FastAPI using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]