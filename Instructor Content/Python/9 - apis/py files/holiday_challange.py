import requests
from datetime import date

def is_today_a_public_holiday(country_code: str) -> bool:
    """
    Checks if today is a public holiday for a given country by querying an API.

    Args:
        country_code (str): The two-letter country code (e.g., "US").

    Returns:
        bool: True if today is a public holiday, False otherwise.

    Raises:
        TypeError: If country_code is not a string.
        ValueError: If country_code is not exactly two characters.
    """
    # Input validation (per requirements)
    if not isinstance(country_code, str):
        raise TypeError("country_code must be a string")
    if len(country_code) != 2:
        raise ValueError("country_code must be a two-letter code")

    today = date.today()
    today_str = today.strftime("%Y-%m-%d")
    current_year = today.year

    url = "https://api.example.com/v1/holidays"
    params = {"country": country_code, "year": current_year}

    response = requests.get(url, params=params)
    holidays = response.json()  # assumed 200 OK per exercise

    return any(holiday.get("date") == today_str for holiday in holidays)
