# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements if you have one, else install packages directly
COPY voicetxt.py .
COPY templates ./templates
COPY static ./static

# Install Python dependencies
RUN pip install --no-cache-dir flask PyPDF2 gTTS


# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["python", "voicetxt.py"]
