Monitoring and Error Tracking with Sentry
=========================================

To improve observability and error tracking, this project integrates with
`Sentry <https://sentry.io>`_. The integration captures unexpected exceptions,
performance issues, and custom logs.

This guide explains how to install, configure, and use Sentry for monitoring.

.. note::
   **Never store secrets or sensitive information in the codebase.**
   Use environment variables instead.

Steps to Integrate Sentry
--------------------------

1. Install Sentry SDK
~~~~~~~~~~~~~~~~~~~~~

In your virtual environment, install the Sentry SDK for Django::

   pip install "sentry-sdk[django]"

2. Configure Sentry
~~~~~~~~~~~~~~~~~~~

Open ``oc_lettings_site/settings.py`` and add the following configuration:

.. code-block:: python

   import sentry_sdk
   from sentry_sdk.integrations.django import DjangoIntegration

   SENTRY_DSN = os.getenv("SENTRY_DSN")  # retrieved from environment variables

   sentry_sdk.init(
       dsn=SENTRY_DSN,
       integrations=[DjangoIntegration()],
       traces_sample_rate=1.0,   # adjust depending on project requirements
       send_default_pii=True,
   )

Set the ``SENTRY_DSN`` variable in your ``.env`` file (never commit this file)::

   SENTRY_DSN=https://<your-key>@oXXXX.ingest.sentry.io/YYYY


.. note::
   This project uses ``python-dotenv`` to load environment variables from a ``.env`` file.
   Make sure to install it in your virtual environment::

       pip install python-dotenv


3. Configure Logging
~~~~~~~~~~~~~~~~~~~~

In ``oc_lettings_site/settings.py``, configure Django’s logging system to use
Python’s built-in logging module:

.. code-block:: python

   LOGGING = {
       "version": 1,
       "disable_existing_loggers": False,
       "handlers": {
           "console": {
               "class": "logging.StreamHandler",
           },
       },
       "root": {
           "handlers": ["console"],
           "level": "INFO",
       },
       "loggers": {
           "django": {
               "handlers": ["console"],
               "level": "INFO",
               "propagate": True,
           },
           "oc_lettings_site": {
               "handlers": ["console"],
               "level": "DEBUG",
               "propagate": False,
           },
       },
   }

This ensures that logs are written to the console (and captured by Render, Docker, or
any logging aggregator).

4. Insert Logs
~~~~~~~~~~~~~~

Use the ``logging`` module in your code at strategic points:

- Inside critical functions
- In ``try/except`` blocks
- For input validation failures

Example (views.py):

.. code-block:: python

   import logging

   logger = logging.getLogger(__name__)

   def letting(request, letting_id):
       try:
           letting_obj = get_object_or_404(Letting, id=letting_id)
           logger.info("Letting %s retrieved successfully", letting_id)
           context = {"title": letting_obj.title, "address": letting_obj.address}
           return render(request, "lettings/letting.html", context)
       except Exception as e:
           logger.error("Unexpected error retrieving letting %s: %s", letting_id, e)
           sentry_sdk.capture_exception(e)
           raise

Deployment Notes
----------------

When deploying to a new environment:

1. Add the ``SENTRY_DSN`` variable to the environment (e.g., ``.env``, Docker secrets, or Render environment variables).
2. Ensure the logging configuration is applied (``settings.py``).
3. Check that logs appear both in the console and in Sentry.
4. Run a test error by forcing an exception locally::

      raise Exception("Sentry test error")

   Verify it appears in the Sentry dashboard.

