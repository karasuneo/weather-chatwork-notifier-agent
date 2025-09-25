#!/usr/bin/env python3
"""天気情報取得のデバッグ用スクリプト"""

import sys
import os
import requests
from dotenv import load_dotenv

# プロジェクトのパスを追加
sys.path.append(
    os.path.join(os.path.dirname(__file__), "src", "weather-chatwork-notifier-agent ")
)

load_dotenv()


def test_direct_api():
    """APIに直接リクエストしてデバッグ"""
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    print(f"API Key: {api_key}")

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": "Tokyo", "appid": api_key, "units": "metric", "lang": "ja"}

    print(f"URL: {base_url}")
    print(f"Params: {params}")

    try:
        response = requests.get(base_url, params=params)
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Text: {response.text}")

        if response.status_code == 200:
            data = response.json()
            print(f"Success: {data}")
        else:
            print(f"Error: {response.text}")

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    test_direct_api()
