# CRUD API using FastAPI

A simple CRUD (Create, Read, Update, Delete) REST API built with FastAPI.

## Features

* Create User
* Read User Data
* Update User Data
* Delete User Data
* Automatic API Documentation with Swagger UI

## Technologies Used

* Python 3.14
* FastAPI
* Uvicorn
* Git & GitHub

## Installation

Clone the repository:

```bash
git clone https://github.com/Rohit43005/Crud.git
cd Crud
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

Run the application:

```bash
python -m uvicorn main:app --reload
```

## API Endpoints

### Home

```http
GET /
```

### About

```http
GET /about
```

### Contact

```http
GET /contact
```

### Create User

```http
POST /create_user
```

Example Request:

```json
{
  "name": "Rohit",
  "age": 21
}
```

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Author

Rohit Darode

B.Tech Electronics and Communication Engineering

MIT-ADT University, Pune
