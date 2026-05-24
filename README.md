# Weather Backend App

## Overview

This project is a backend weather application built using FastAPI and SQLite.

The application retrieves live weather data from the Open-Meteo API and provides full CRUD functionality for storing and managing weather records.

---

## Features

- Live weather API integration
- FastAPI backend architecture
- SQLite database persistence
- Full CRUD operations
- JSON export endpoint
- Swagger API documentation

---

## Technologies Used

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Uvicorn
- Requests

---

## Project Structure

```bash
weather-backend-app/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── crud.py
│   └── weather_api.py
│
├── weather.db
├── requirements.txt
├── README.md
```

---

## API Endpoints

### Weather API

| Method | Endpoint | Description |
|---|---|---|
| GET | `/weather/{location}` | Get live weather data |

---

### CRUD Operations

| Method | Endpoint | Description |
|---|---|---|
| POST | `/weather/save/{location}` | Save weather record |
| GET | `/records` | Read all records |
| PUT | `/records/{record_id}` | Update weather record |
| DELETE | `/records/{record_id}` | Delete weather record |

---

### Export

| Method | Endpoint | Description |
|---|---|---|
| GET | `/export/json` | Export records as JSON |

---

## Database

SQLite was used for persistent weather record storage.

Stored fields include:
- Location
- Temperature
- Wind Speed
- Weather Code

---

## How to Run

### 1. Clone Repository

```bash
git clone <your-repository-link>
cd weather-backend-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

## Swagger Documentation

After running the server, open:

```text
http://127.0.0.1:8000/docs
```

to access interactive API documentation.

---

## Demo Video

[Paste Demo Video Link Here](https://drive.google.com/file/d/1VjhYcJ6dwLnz_F0k2LHaP5G08gbdLfMP/view?usp=sharing)

---

## Future Improvements

- User authentication
- PostgreSQL integration
- Forecast endpoints
- Docker deployment
- Additional API integrations

---

## Author

Keya Chaudhari