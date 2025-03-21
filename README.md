# FastAPI MVC App

This is a FastAPI-based web application. The application supports user authentication, post management, and caching for optimized performance.

## Features

- **User Authentication** (Signup & Login with JWT-based token authentication)
- **Post Management** (Add, Retrieve, and Delete posts)
- **Caching** (5-minute caching for improved performance)
- **Dependency Injection**
- **SQLAlchemy ORM** for interaction with SQLDB
- **Field Validation** using Pydantic models

## Requirements

- FastAPI
- SQLAlchemy
- PyJWT
- Cachetools

## Install dependencies

```bash
pip install -r requirements.txt
```

## Endpoints

### Authentication

- **POST** `/auth/signup` — Create a new user
- **POST** `/auth/login` — Login and receive an access token

### Posts

- **POST** `/posts` — Add a new post
- **GET** `/posts` — Retrieve all posts (with caching)
- **DELETE** `/posts/{post_id}` — Delete a specific post

## Usage

1. **Signup:** Create an account with your `email` and `password`.
2. **Login:** Authenticate to receive a JWT token.
3. Use the JWT token for authentication when adding, retrieving, or deleting posts.
