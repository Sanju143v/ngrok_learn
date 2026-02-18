# FastAPI User API

A FastAPI project with User CRUD operations using SQLAlchemy and Vercel Postgres.

## Project Structure
```
.
├── app/
│   ├── models/
│   │   └── user.py
│   ├── schemas/
│   │   └── user.py
│   ├── routes/
│   │   └── user_routes.py
│   ├── repositories/
│   │   └── user_repository.py
│   └── database.py
├── main.py
├── requirements.txt
├── vercel.json
└── .env
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create `.env` file:
```
DATABASE_URL=postgresql://user:password@host/database
```

3. Run the application:
```bash
uvicorn main:app --reload
```

## API Endpoints

- `GET /` - Hello World
- `POST /users/` - Create a new user
- `GET /users/` - Get all users
- `GET /users/{user_id}` - Get user by ID

## Deployment to Vercel

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Deploy:
```bash
vercel
```

3. Set environment variable in Vercel:
```bash
vercel env add DATABASE_URL
```
