"""天気情報を取得するツール"""

import os
import requests
from datetime import datetime


def get_weather(location: str) -> dict:
    """
    指定された場所の現在の天気情報を取得する

    Args:
        location: 都市名（例：Tokyo, Osaka, New York）

    Returns:
        天気情報を含む辞書
    """
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric",
        "lang": "ja"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    return {
        "location": f"{data['name']}, {data['sys'].get('country', '')}",
        "datetime": datetime.fromtimestamp(data['dt']).strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": data['main']['temp'],
        "feels_like": data['main']['feels_like'],
        "description": data['weather'][0]['description'],
        "humidity": data['main']['humidity'],
        "wind_speed": data['wind']['speed']
    }