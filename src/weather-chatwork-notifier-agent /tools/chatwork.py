"""ChatWork APIを使用したツール群"""

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
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"body": message}

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()

    result = response.json()
    return {
        "status": "success",
        "message_id": result.get("message_id"),
        "room_id": room_id,
        "report": f"メッセージを送信しました (ID: {result.get('message_id')})",
    }


def get_room_info() -> dict:
    """
    ChatWorkの設定されたルームの情報を取得する
    環境変数CHATWORK_ROOM_IDで指定されたルーム情報を取得

    Returns:
        ルーム情報を含む辞書
    """
    api_key = os.getenv("CHATWORK_API_TOKEN")
    room_id = os.getenv("CHATWORK_ROOM_ID")

    if not api_key:
        return {"status": "error", "message": "CHATWORK_API_TOKEN not set"}

    if not room_id:
        return {"status": "error", "message": "CHATWORK_ROOM_ID not set"}

    url = f"https://api.chatwork.com/v2/rooms/{room_id}"
    headers = {
        "X-ChatWorkToken": api_key,
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        result = response.json()
        return {
            "status": "success",
            "room_id": result.get("room_id"),
            "name": result.get("name"),
            "type": result.get("type"),
            "role": result.get("role"),
            "sticky": result.get("sticky"),
            "unread_num": result.get("unread_num"),
            "mention_num": result.get("mention_num"),
            "mytask_num": result.get("mytask_num"),
            "message_num": result.get("message_num"),
            "file_num": result.get("file_num"),
            "task_num": result.get("task_num"),
            "icon_path": result.get("icon_path"),
            "last_update_time": result.get("last_update_time"),
            "description": result.get("description"),
            "report": f"ルーム情報を取得しました: {result.get('name')} (ID: {result.get('room_id')})",
        }
    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": f"API request failed: {str(e)}",
            "report": f"ルーム情報の取得に失敗しました: {str(e)}",
        }
