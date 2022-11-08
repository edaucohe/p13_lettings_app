# Pull the official base image
FROM python:3.9.4-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# Set work directory
WORKDIR /app

# Copy project
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 8000 for access from other applications
# EXPOSE $PORT

# Set the executable commands in the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:${PORT##\\}"]
