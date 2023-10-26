Django image hosting site

Environment: Windows11 terminal, Visual Studio Code, SQLite Viewer, Django 4.1.5, Python 3.9.13

Language: Python

Functions:
- User registration, Login and Logout
- Posting a photo and a comment, and deleting them
- Every user can read(watch) and delete all photos and comments
- Enlarging a photo with clicking it
- Pagination

You need to install Imaging Library Pillow.

>python -m pip install Pillow

Tests: /timeline/tests.py

3 tests:
- testing image & comment posting form
- login test whether users are redirected to login page if they're not authenticated
- login test whether login with invalid username & password fails