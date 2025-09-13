Database Structure
==================

This section describes the structure of the database and the main data models used in the project.

Models
------

### Address (lettings app)

Represents a physical address.

- **number**: Positive integer, max value 9999.
- **street**: CharField, max length 64.
- **city**: CharField, max length 64.
- **state**: CharField, exactly 2 characters.
- **zip_code**: Positive integer, max value 99999.
- **country_iso_code**: CharField, exactly 3 characters.

__String representation__: Returns the address in the format `"{number} {street}"`.

### Letting (lettings app)

Represents a letting with a title and an associated address.

- **title**: CharField, max length 256.
- **address**: One-to-one relationship with `Address`. Deletes the address if the letting is deleted.

__String representation__: Returns the letting title.

### Profile (profiles app)

Represents a user profile with an optional favorite city.

- **user**: One-to-one relationship with Django's built-in `User` model.
- **favorite_city**: Optional CharField, max length 64.

__String representation__: Returns the username of the associated user.


Local Database Access
---------------------


1. Open a SQLite session::

   sqlite3 oc-lettings-site.sqlite3

2. Show tables::

   .tables

3. Show table columns::

   pragma table_info(Python-OC-Lettings-FR_profile);

4. Example query::

   select user_id, favorite_city
   from Python-OC-Lettings-FR_profile
   where favorite_city like 'B%';

5. Quit::

   .quit
