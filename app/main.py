from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud
from app.database import engine
from app import models
from fastapi import FastAPI, HTTPException
from app.weather_api import get_current_weather

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {
        "message": "Weather Backend API is running"
    }


@app.get("/weather/{location}")
def weather(location: str):
    data = get_current_weather(location)

    if data is None:
        raise HTTPException(status_code=404, detail="Location not found or weather API failed")

    return data

@app.post("/weather/save/{location}")
def save_weather(location: str, db: Session = Depends(get_db)):
    data = get_current_weather(location)

    if data is None:
        raise HTTPException(status_code=404, detail="Location not found")

    current = data["current_weather"]

    record = crud.create_weather_record(
        db=db,
        location=location,
        temperature=current["temperature"],
        windspeed=current["windspeed"],
        weathercode=current["weathercode"]
    )

    return record


@app.get("/records")
def read_records(db: Session = Depends(get_db)):
    return crud.get_weather_records(db)

@app.put("/records/{record_id}")
def update_record(
    record_id: int,
    new_location: str,
    db: Session = Depends(get_db)
):

    updated = crud.update_weather_record(
        db,
        record_id,
        new_location
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Record not found"
        )

    return updated

@app.delete("/records/{record_id}")
def delete_record(
    record_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_weather_record(
        db,
        record_id
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Record not found"
        )

    return deleted

@app.get("/export/json")
def export_json(
    db: Session = Depends(get_db)
):

    records = crud.get_weather_records(db)

    return records