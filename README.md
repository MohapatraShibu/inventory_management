# Inventory Management API

## Setup Instructions

1. Clone the repository.

2. Install the dependencies:
   pip install -r requirements.txt

3. Setup PostgreSQL database and update settings.py.

4. Run migrations:
python manage.py migrate

5. Start Redis:
redis-server

6. Run the Django server:
python manage.py runserver

7. Use http://localhost:8000/api/items/ to access the item endpoints.

8. Run tests:
python manage.py test

9. API Endpoints
* POST /api/register/: Register a new user.
* POST /api/login/: Login and get JWT token.
* GET /api/items/: Get a list of items.
* POST /api/items/: Create a new item.
* GET /api/items/<item_id>/: Get details of an item.
* PUT /api/items/<item_id>/: Update an item.
* DELETE /api/items/<item_id>/: Delete an item.

10. Caching
* Item details are cached for 15 minutes using Redis.