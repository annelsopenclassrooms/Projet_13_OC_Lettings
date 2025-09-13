Quickstart Guide
================

1. **Start the development server:**

   .. code-block:: bash

      cd /path/to/Python-OC-Lettings-FR
      source venv/bin/activate
      python manage.py runserver

2. **Open your browser at:** ``http://localhost:8000``

3. **Confirm the website is working and navigation is possible.**
   You should see several profiles and lettings.

Admin Panel
-----------

- **Visit:** ``http://localhost:8000/admin``
- **Login:**
  - Username: ``admin``
  - Password: ``Abc1234!``

Linting
-------

**Run Flake8 to check code style:**

.. code-block:: bash

   flake8

Unit Tests
----------

**Run pytest to execute the test suite:**

.. code-block:: bash

   pytest
