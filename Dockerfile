# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install flask

# Run the app
CMD ["python", "app.py"]
