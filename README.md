# Employee Management API

A RESTful Employee Management API built using FastAPI, SQLAlchemy, and SQLite.

## Features

- Create Employee
- Get All Employees
- Get Employee by ID
- Update Employee
- Delete Employee
- Input Validation using Pydantic
- HTTP Error Handling
- Interactive Swagger API Documentation

## Tech Stack

- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Git & GitHub

## Project Structure

```
employee-api/
│
├── app/
│   ├── main.py
│   ├── crud.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

```bash
git clone https://github.com/deepaksaranay/employee-management-api.git

cd employee-management-api

python -m venv .venv

.\.venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

## API Documentation

After running the server:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home |
| POST | /employees | Create Employee |
| GET | /employees | Get All Employees |
| GET | /employees/{id} | Get Employee by ID |
| PUT | /employees/{id} | Update Employee |
| DELETE | /employees/{id} | Delete Employee |

## Future Improvements

- PostgreSQL
- JWT Authentication
- Docker
- Unit Testing
- Deployment
