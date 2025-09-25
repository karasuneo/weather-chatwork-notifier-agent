"""都市名から緯度経度を取得するツール"""

import os
import requests


def get_coordinates_from_city(city_name: str) -> dict:
    """
    都市名から緯度経度を取得する（OpenWeatherMap Geocoding API使用）

    Args:
        city_name: 都市名（例：Tokyo, Osaka, New York）

    Returns:
        緯度経度情報を含む辞書
    """
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        return {"status": "error", "message": "OPENWEATHERMAP_API_KEY not set"}

    base_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {"q": city_name, "limit": 1, "appid": api_key}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if not data:
            return {
                "status": "error",
                "message": f"City '{city_name}' not found",
                "report": f"都市「{city_name}」が見つかりませんでした",
            }

        location_info = data[0]
        return {
            "status": "success",
            "city_name": location_info.get("name", city_name),
            "country": location_info.get("country", ""),
            "state": location_info.get("state", ""),
            "latitude": location_info.get("lat"),
            "longitude": location_info.get("lon"),
            "report": f"{location_info.get('name', city_name)}, {location_info.get('country', '')}の座標を取得しました (緯度: {location_info.get('lat')}, 経度: {location_info.get('lon')})",
        }
    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": f"API request failed: {str(e)}",
            "report": f"座標の取得に失敗しました: {str(e)}",
        }
