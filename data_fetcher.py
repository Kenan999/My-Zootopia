import os
import requests


API_BASE_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.environ.get("API_KEY")


def fetch_data(animal_name):
    if not API_KEY:
        raise ValueError("API_KEY environment variable is not set.")

    response = requests.get(
        API_BASE_URL,
        headers={"X-Api-Key": API_KEY},
        params={"name": animal_name},
        timeout=10,
    )

    response.raise_for_status()
    return response.json()