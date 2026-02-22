# Django/Angular Driver Assignments Dashboard

A tiny transportation logistics demo with a Django REST API and an Angular Material dashboard for managing driver assignments.

## Video

https://github.com/user-attachments/assets/b7780408-00c4-4f36-b322-5cab7fe71fc5

## Features

- Assignment table — lists routes with start/end location, distance, and status
- Driver assignment — each row has a dropdown to assign or unassign a driver
  - Conflict prevention — drivers already assigned to another route are disabled in all other dropdowns
  - Bidirectional sync — reassigning a driver automatically unassigns them from their previous route
- REST API — Django REST Framework with `GET`, `POST`, and `PUT` endpoints for assignments and drivers
- Small test suite with `pytest`

## Stack
Django, Django REST Framework, Angular, and SQLite

## Running with Docker

```bash
docker compose up --build
```
Open http://localhost:4200. To stop and remove data: `docker compose down -v`



## Running locally

Backend:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed
python manage.py runserver
```

Frontend:

```bash
cd frontend
npm install
ng serve
```

Open [http://localhost:4200](http://localhost:4200). The backend must be running on port 8000.

Tests:

```bash
cd backend
source .venv/bin/activate
pytest
```
