# restful_apy
RESTful API implementation written in Python, using Django as a framework and SQLite as db

# Required dependencies:
- python3 3.2.19
- pip
- Django
- Django REST Framework

## Instructions
1. clone repo
2. cd restful_apy
3. source ./django_env/bin/activate
4. python3 manage.py migrate
5. python3 manage.py runserver
6. Visit http://127.0.0.1:8000/admin/
7. Visit http://127.0.0.1:8000/tasks/api

Sample JSON data for POST method
{
    "title": "Title goes here",
    "description": "Description contents go here",
    "creation_date": "2025-02-20",
    "due_date": "2025-02-24",
    "status": "completed"
}
