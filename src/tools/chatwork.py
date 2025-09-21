"""ChatWorkにメッセージを送信するツール"""

import os
import requests


def send_chatwork_message(room_id: str, message: str) -> dict:
    """
    ChatWorkの指定されたルームにメッセージを送信する

    Args:
        room_id: 送信先のルームID
        message: 送信するメッセージ

    Returns:
        送信結果を含む辞書
    """
    api_key = os.getenv("CHATWORK_API_TOKEN")
    if not api_key:
        return {"status": "error", "message": "CHATWORK_API_TOKEN not set"}

    url = f"https://api.chatwork.com/v2/rooms/{room_id}/messages"
    headers = {
        "X-ChatWorkToken": api_key,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"body": message}

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()

    result = response.json()
    return {
        "status": "success",
        "message_id": result.get("message_id"),
        "room_id": room_id,
        "report": f"メッセージを送信しました (ID: {result.get('message_id')})"
    }