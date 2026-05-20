from sqlalchemy import Column, Integer, String, Float

from app.database import Base


class WeatherRecord(Base):

    __tablename__ = "weather_records"

    id = Column(Integer, primary_key=True, index=True)

    location = Column(String, index=True)

    temperature = Column(Float)

    windspeed = Column(Float)

    weathercode = Column(Integer)