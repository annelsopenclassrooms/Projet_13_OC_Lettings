Deployment
==========

The application can be deployed using:

- Docker
- Render
- Google Cloud Run
- GitHub Actions CI/CD pipeline

Steps
-----

1. **Build the Docker image:**

   .. code-block:: bash

      docker build -t oc-lettings .

2. **Run locally with Docker:**

   .. code-block:: bash

      docker run -p 8000:8000 oc-lettings

3. **Deploy to your preferred cloud provider** (Render, GCP, or others).
Deployment
==========

This section describes how the CI/CD pipeline and deployment of the OC Lettings project is structured. 
The documentation is intended to allow your successor to deploy the site without any issues.

CI/CD Pipeline Overview
-----------------------

The pipeline consists of **three main jobs**:

1. **Build and Test**

   - Reproduces the local development environment.
   - Executes linting using ``flake8``.
   - Runs the test suite using ``pytest``.
   - Checks that test coverage is above 80%.

2. **Containerization**

   - Builds a Docker image of the site.
   - Pushes the image to Docker Hub.
   - Tags the image with a distinct label (e.g., the commit hash).
   - Allows running the site locally using the Docker image.
   - Provides a single command to build, tag, and run the image locally.

3. **Deployment**

   - Deploys the site to the chosen hosting provider (Render, AWS WebApp, Azure, etc.).
   - Triggered **only** for commits pushed to the ``master`` branch.
   - The deployment job runs only if the containerization job succeeds.
   - Branches other than ``master`` only trigger the build and test jobs (no deployment or containerization).

Deployment Requirements
-----------------------

- Docker and Docker Hub account.
- Access to the chosen hosting provider (e.g., Render account).
- Environment variables set correctly (e.g., ``SECRET_KEY``, ``SENTRY_DSN``, database credentials).
- Static files correctly collected and available in ``STATIC_ROOT``.
- The production Django settings (``DEBUG=False``, ``ALLOWED_HOSTS`` configured for the domain).

Deployment Steps
----------------

1. **Trigger the pipeline**

   - Push changes to the ``master`` branch on GitHub.
   - GitHub Actions automatically triggers the pipeline.

2. **Build and Test**

   - The pipeline reproduces the local environment.
   - Runs linting: ``flake8``.
   - Runs tests: ``pytest``.
   - Checks coverage (>80%).
   - If any of these steps fail, the pipeline stops.

3. **Containerization**

   - If build and tests succeed, a Docker image is created and tagged with the commit hash.
   - The image is pushed to Docker Hub.
   - The image can be pulled locally using::

       docker pull <docker-username>/oc-lettings:<commit-hash>
       docker run -p 8000:8000 <docker-username>/oc-lettings:<commit-hash>

   - Verify the site runs locally in Docker.

4. **Production Deployment**

   - Only executes if containerization succeeds.
   - The hosting provider (e.g., Render) pulls the latest Docker image from Docker Hub.
   - The site is deployed with environment variables configured in the hosting dashboard.
   - Verify static files and templates load correctly.
   - Confirm that the admin interface is fully functional and styled correctly.

Notes
-----

- All sensitive data (Sentry DSN, SECRET_KEY, database credentials) must **not** be stored in code; always use environment variables.
- The deployed site must visually match the local environment.
- The successor should be able to redeploy or rollback using the same pipeline without additional troubleshooting.
