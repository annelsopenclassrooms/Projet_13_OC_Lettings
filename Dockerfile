# Use Python 3.12 as base image
FROM python:3.12-slim
# Set working directory inside the container
WORKDIR /app
# Install system dependencies (required for some Python packages)
RUN apt-get update && apt-get install -y --no-install-recommends gcc python3-dev && rm -rf /var/lib/apt/lists/*
# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Install gunicorn and whitenoise
RUN pip install --no-cache-dir gunicorn whitenoise
# Copy the rest of the application code
COPY . .
# Create staticfiles directory and set permissions
RUN mkdir -p /app/staticfiles && chmod -R 755 /app/staticfiles
# Collect Django static files
# RUN python manage.py collectstatic --noinput
# Expose the port Django will run on
EXPOSE 8000
# Default command to run the Django app with Gunicorn
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
