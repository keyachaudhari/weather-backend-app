import requests


def get_current_weather(location: str):

    # Step 1: Convert city name to coordinates
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_response = requests.get(
        geo_url,
        params={"name": location, "count": 1}
    )

    geo_data = geo_response.json()

    if "results" not in geo_data:
        return None

    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]

    # Step 2: Get weather using coordinates
    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_response = requests.get(
        weather_url,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True
        }
    )

    return weather_response.json()