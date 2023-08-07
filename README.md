# Practical Test - Developer

This is an example API application built with Python and Flask.

## Settings

1. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy env from example and generate a key

```bash
cp .env.example .env
python app/console/commands/generate_key.py
```

## Database Migrations

To create and apply database migrations, run the following command:

```bash
alias flask='python -m flask'
flask db init
flask db migrate
flask db upgrade
```

## Execution

To run the application, use the following command:

```bash
flask run
```

The application will be available at http://localhost:5000.

## Routes

- /api/users - Route to create a new user (POST).
- /api/users/<id> - Route to view, update or delete a user (GET, PUT, DELETE).

Routes protected by JWT authentication (PUT, DELETE).

## Authentication

To authenticate, make a POST request to /api/auth/login with a JSON in the request body containing the authentication information (username and password). This will return a JWT token that can be used to access protected routes.
