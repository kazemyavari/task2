from pyowm import OWM
from pyowm.utils import config
from typing import Dict, Tuple
from django.core.cache import cache
from django.conf import settings
import re


def _get_weather_from_API(city: str, country: str, zip_code: int) -> Dict:
    """Fetch weather data from the OpenWeatherMap API.

    Args:
        city (str): The name of the city.
        country (str): The name of the country.
        zip_code (int): The postal code of the location.

    Returns:
        dict: A dictionary containing weather information.

    Raises:
        pyowm.exceptions.api_call_error.APIRequestError: If an error occurs during the API request.
    """
    owm = OWM(settings.WEATHER_API_KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(f"{city},{country}")
    observation = mgr.weather_at_zip_code(zip_code, observation.location.country)
    return observation.weather.to_dict()


def _parse_address(address: str) -> Tuple[str]:
    """Parse an address string to extract city, country, and zip code.

    Args:
        address (str): The address string.

    Returns:
        tuple: A tuple containing city, country, and zip code.

    Example:
        >>> _parse_address("Street 1, 10115 Berlin, Germany")
        ('Berlin', 'Germany', '10115')
    """
    pattern = r"(\d+)\s*([^,]+),\s*([^,]+)$"
    match = re.search(pattern, address)

    if not match:
        return None

    zip_code = match.group(1)
    city = match.group(2).strip()
    country = match.group(3).strip()
    return city, country, zip_code


def get_weather(address: str) -> Dict:
    """Get weather information for a given address.

    Args:
        address (str): The address for which weather information is requested.

    Returns:
        dict: A dictionary containing weather information.

    Example:
        >>> get_weather("Street 1, 10115 Berlin, Germany")
        {'temp': 20, 'status': 'Clear', ...}
    """
    city, country, zip_code = _parse_address(address)
    cache_key = f"weather_{city}_{country}_{zip_code}"
    cached_data = cache.get(cache_key)

    if cached_data:
        return cached_data

    weather_data = _get_weather_from_API(city, country, zip_code)
    cache.set(cache_key, weather_data, settings.WEATHER_EXPIR_TIME)
    return weather_data
