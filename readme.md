# Simple Business Finance API

A simple and practical finance tracking API built with Flask. It allows you to manage sales and expenses, generate financial reports, and handle user authentication via JWT. Designed to be clean, modular, and easy to integrate with a frontend.

---

## How it Works

The API is structured into clear modules:

* **Authentication**: Users register and log in to receive a JWT. This token must be included in requests to access protected routes.
* **Sales & Expenses**: After authentication, users can create, list, update, and delete sales or expense entries.
* **Reports**: The API provides a summary endpoint that aggregates sales and expenses, returning the total revenue, total expenses, and profit.

All interactions are JSON-based and secured with JWT tokens. The API also includes automatic Swagger documentation for easy testing.

---

## Stack

* **Backend**: Flask + Flask-SQLAlchemy
* **Database**: PostgreSQL
* **Auth**: JWT (Flask-JWT-Extended)
* **Docs**: Swagger UI via Flasgger
* **Tests**: Pytest + Coverage
* **Dockerized**: Full support for Docker and docker-compose

---

## Installation

### Using Docker

```bash
git clone https://github.com/yourusername/business-finance-api.git
cd business-finance-api
docker-compose up --build
```

The API will be available at: `http://localhost:5000`
Swagger UI: `http://localhost:5000/apidocs`

### Without Docker (Manual Setup)

1. **Set up virtual environment**:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Configure environment variables** (create a `.env` file):

```
DATABASE_URL=postgresql://admin:admin123@localhost:5432/smallbiz_db
JWT_SECRET_KEY=your_secret_key
```

4. **Run migrations**:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

5. **Start the application**:

```bash
flask run
```

---

## Authentication

After registering via `/api/auth/register`, users log in through `/api/auth/login` and receive a token like:

```
Authorization: Bearer <your_token>
```

Include this in headers for all protected endpoints.

---

## Endpoints Summary

| Method | Endpoint             | Description                  |
| ------ | -------------------- | ---------------------------- |
| POST   | /api/auth/register   | Register a new user          |
| POST   | /api/auth/login      | Login and receive JWT token  |
| GET    | /api/expenses        | List all expenses            |
| POST   | /api/expenses        | Create a new expense         |
| PUT    | /api/expenses/       | Update an expense            |
| DELETE | /api/expenses/       | Delete an expense            |
| GET    | /api/sales           | List all sales               |
| POST   | /api/sales           | Create a new sale            |
| PUT    | /api/sales/          | Update a sale                |
| DELETE | /api/sales/          | Delete a sale                |
| GET    | /api/reports/summary | Get financial summary report |

---

## Documentation

Swagger UI is automatically generated and available at:

```
http://localhost:5000/apidocs
```

---

## Testing

Run the test suite with coverage:

```bash
pytest --cov=app
```

All core features are covered by tests to ensure reliability.

---

## CI/CD

You can set up GitHub Actions to run tests on every push. Even without deploying the app, the tests will run using Docker in the CI pipeline. For that, make sure to provide a `.env.ci` or mock DB configuration suitable for test containers.

---


## License

MIT License
