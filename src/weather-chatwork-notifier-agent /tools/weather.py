"""天気情報を取得するツール"""

import os
import requests



def get_weather_by_coordinates(latitude: float, longitude: float) -> dict:
    """
    緯度経度から天気情報を取得する

    Args:
        latitude: 緯度
        longitude: 経度

    Returns:
        天気情報を含む辞書
    """
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        return {"status": "error", "message": "OPENWEATHERMAP_API_KEY not set"}

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "units": "metric",
        "lang": "ja",
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # データの存在確認
        if (
            "name" not in data
            or "sys" not in data
            or "main" not in data
            or "weather" not in data
        ):
            return {"status": "error", "message": "Invalid API response format"}

        # 安全にデータを取得
        location_name = data.get("name", "Unknown")
        country = data.get("sys", {}).get("country", "")
        main_data = data.get("main", {})
        weather_data = data.get("weather", [{}])[0] if data.get("weather") else {}
        wind_data = data.get("wind", {})

        return {
            "status": "success",
            "location": f"{location_name}, {country}" if country else location_name,
            "latitude": latitude,
            "longitude": longitude,
            "temperature": main_data.get("temp"),
            "feels_like": main_data.get("feels_like"),
            "description": weather_data.get("description", "情報なし"),
            "humidity": main_data.get("humidity"),
            "wind_speed": wind_data.get("speed"),
            "report": f"{location_name}の天気情報を取得しました: {weather_data.get('description', '情報なし')}, 気温{main_data.get('temp', '不明')}°C",
        }
    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": f"API request failed: {str(e)}",
            "report": f"天気情報の取得に失敗しました: {str(e)}",
        }
