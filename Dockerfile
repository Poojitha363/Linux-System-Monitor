# Base Python image
FROM python:3.12

# Working directory inside container
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install psutil

# Run the application
CMD ["python", "monitor.py"]