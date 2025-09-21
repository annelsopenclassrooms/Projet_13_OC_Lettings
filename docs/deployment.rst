Deployment and Production Management
===================================

This section explains how to deploy and manage the OC Lettings application in a production environment.
It covers the CI/CD pipeline, Docker, Render deployment, and environment secrets.

CI/CD Pipeline
--------------

The CI/CD pipeline is composed of three main jobs:

1. **Build and Test**
   - Reproduces the local development environment.
   - Installs dependencies and runs linting with `flake8`.
   - Runs the test suite with `pytest`.
   - Checks that code coverage is above 80%.
   - Only successful tests allow the next steps to execute.

2. **Docker Build and Push**
   - Builds a Docker image of the application.
   - Tags the image with the commit SHA and `latest`.
   - Pushes the image to Docker Hub.
   - This step runs **only if tests pass** and only on the `master` branch.

3. **Deployment**
   - Pulls the Docker image from Docker Hub.
   - Deploys the application on Render using the linked Docker repository.
   - This step runs **only if the Docker build succeeds** and only on the `master` branch.

GitHub Actions Example
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: yaml

    name: CI/CD Pipeline

    on:
      push:
        branches:
          - master
          - dev
      pull_request:
        branches:
          - master
          - dev

    jobs:
      # Build and Test job
      build-and-test:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v3
          - uses: actions/setup-python@v4
            with:
              python-version: 3.12
          - run: |
              python -m venv venv
              source venv/bin/activate
              pip install --upgrade pip
              pip install -r requirements.txt
          - run: |
              source venv/bin/activate
              flake8 .
          - run: |
              source venv/bin/activate
              python manage.py migrate
              pytest --cov=. --cov-fail-under=80

      # Docker Build job
      docker-build:
        needs: build-and-test
        runs-on: ubuntu-latest
        if: github.ref == 'refs/heads/master'
        steps:
          - uses: actions/checkout@v3
          - uses: docker/login-action@v2
            with:
              username: ${{ secrets.DOCKER_USERNAME }}
              password: ${{ secrets.DOCKER_PASSWORD }}
          - run: |
              docker build -t ${{ secrets.DOCKER_USERNAME }}/oc-lettings-site:${{ github.sha }} .
              docker tag ${{ secrets.DOCKER_USERNAME }}/oc-lettings-site:${{ github.sha }} ${{ secrets.DOCKER_USERNAME }}/oc-lettings-site:latest
              docker push ${{ secrets.DOCKER_USERNAME }}/oc-lettings-site:${{ github.sha }}
              docker push ${{ secrets.DOCKER_USERNAME }}/oc-lettings-site:latest

      # Deployment job
      deploy:
        needs: docker-build
        runs-on: ubuntu-latest
        if: github.ref == 'refs/heads/master'
        steps:
          - uses: actions/checkout@v3
          - run: |
              docker login -u ${{ secrets.DOCKER_USERNAME }} -p ${{ secrets.DOCKER_PASSWORD }}
              docker pull ${{ secrets.DOCKER_USERNAME }}/oc-lettings-site:latest
              echo "Deploying to Render via linked Docker Hub repository."

Environment Variables and Secrets
---------------------------------

The CI/CD pipeline and production environment rely on several **secrets**. Never commit these values to the repository.

**List of Secrets**

- **SECRET_KEY**
  - Django secret key used for sessions, CSRF, and password hashing.
- **SENTRY_DSN**
  - Sentry Data Source Name for error logging and monitoring.
- **ALLOWED_HOSTS**
  - List of hosts allowed to serve the Django application.
- **DOCKER_USERNAME**
  - Docker Hub account username.
- **DOCKER_PASSWORD**
  - Docker Hub access token or password.

**Configuration**

- **GitHub Actions**
  - Go to **Repository → Settings → Secrets and variables → Actions**.
  - Add the secrets listed above.
- **Render**
  - Go to your Render web service → Environment tab.
  - Add the secrets as environment variables.
  - Redeploy the service.

Best Practices
^^^^^^^^^^^^^

- Never hardcode secrets in your code.
- Use different secrets for development, staging, and production.
- Rotate secrets if compromised.
- Use `.env` with `python-dotenv` for local development.

Static Files
------------

- The production server uses **Whitenoise** to serve static files.
- Run ``python manage.py collectstatic`` before deployment.
- Make sure all assets referenced in CSS/JS exist in the `static` folder.

Production Settings Checklist
-----------------------------

- `DEBUG = False`
- `SECRET_KEY` set via environment variable
- `ALLOWED_HOSTS` includes the production domain
- Sentry DSN configured
- Static files collected
- Docker image tested locally
- CI/CD pipeline passing all tests

