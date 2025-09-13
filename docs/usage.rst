Usage Guide
===========

This section explains how to use the Orange County Lettings website as a visitor. 
All users can browse lettings and profiles without authentication. Administration tasks are done through the Django admin panel.

Browsing Lettings
-----------------

- Go to the lettings index page.
- All lettings are listed with their title and address.
- Click on a letting title to view detailed information including the full address.

Example URL patterns:

- `/lettings/` → displays all lettings
- `/lettings/<letting_id>/` → displays details for a single letting

Browsing Profiles
-----------------

- Go to the profiles index page.
- All user profiles are listed.
- Click on a username to view the user's profile details including their favorite city.

Example URL patterns:

- `/profiles/` → displays all profiles
- `/profiles/<username>/` → displays details for a single profile

Notes
-----

- No login or registration is required to browse the site.
- All modifications and management of lettings or profiles are handled via the Django admin panel at `/admin/`.

