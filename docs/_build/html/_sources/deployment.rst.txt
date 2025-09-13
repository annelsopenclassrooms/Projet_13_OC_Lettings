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
