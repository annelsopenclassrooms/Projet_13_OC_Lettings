Installation Instructions
=========================

Prerequisites
-------------
- GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.6 or higher

On macOS / Linux
----------------
1. Clone the repository::

   .. code-block:: bash

      cd /path/to/put/project/in
      git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git

2. Create and activate a virtual environment::

   .. code-block:: bash

      cd /path/to/Python-OC-Lettings-FR
      python -m venv venv
      source venv/bin/activate

   .. note::
      On Ubuntu, you may need to install venv first:

      .. code-block:: bash

         apt-get install python3-venv

3. Install dependencies::

   .. code-block:: bash

      pip install --requirement requirements.txt

On Windows
----------
Using PowerShell:

.. code-block:: powershell

   .\venv\Scripts\Activate.ps1

Replace ``which <my-command>`` with:

.. code-block:: powershell

   (Get-Command <my-command>).Path
