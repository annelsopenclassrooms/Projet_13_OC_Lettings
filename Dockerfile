# Use Python 3.12 as base image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ensure gunicorn is installed
RUN pip install --no-cache-dir gunicorn

# Copy the rest of the application code
COPY . .

# Collect Django static files
RUN python manage.py collectstatic --noinput

# Expose the port Django will run on
EXPOSE 8000

# Default command to run the Django app with Gunicorn
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
