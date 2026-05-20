from sqlalchemy.orm import Session
from app import models


def create_weather_record(
    db: Session,
    location: str,
    temperature: float,
    windspeed: float,
    weathercode: int
):
    record = models.WeatherRecord(
        location=location,
        temperature=temperature,
        windspeed=windspeed,
        weathercode=weathercode
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record


def get_weather_records(db: Session):
    return db.query(models.WeatherRecord).all()

def update_weather_record(
    db: Session,
    record_id: int,
    new_location: str
):

    record = db.query(models.WeatherRecord).filter(
        models.WeatherRecord.id == record_id
    ).first()

    if not record:
        return None

    record.location = new_location

    db.commit()
    db.refresh(record)

    return record

def delete_weather_record(
    db: Session,
    record_id: int
):

    record = db.query(models.WeatherRecord).filter(
        models.WeatherRecord.id == record_id
    ).first()

    if not record:
        return None

    db.delete(record)

    db.commit()

    return {
        "message": "Record deleted successfully"
    }