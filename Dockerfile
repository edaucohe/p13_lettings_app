# Pull the official base image
FROM python:3.9.4

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Expose port 8000 for access from other applications
EXPOSE 8000

# Set the executable commands in the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
