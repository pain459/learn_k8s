# Start from a lightweight Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the Python server script into the image
COPY log_server.py /app/log_server.py

# Expose the port that the HTTP server listens on
EXPOSE 8080

# Run the Python log server
CMD ["python", "/app/log_server.py"]
