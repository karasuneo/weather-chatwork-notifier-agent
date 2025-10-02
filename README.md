# Weather Chatwork Notifier Agent

天気情報を取得してChatWorkに通知するエージェントシステム

## 機能

- **天気情報取得**: OpenWeatherMap APIを使用した天気情報の取得
- **ChatWork通知**: 指定されたChatWorkルームへのメッセージ送信
- **座標ベース取得**: 都市名から座標を取得して確実な天気情報取得
- **ルーム情報取得**: ChatWorkルームの詳細情報を取得

## セットアップ

### 1. 依存関係のインストール

```bash
uv sync
```

### 2. 環境変数の設定

`.env.example`を`.env`にコピーして必要な値を設定：

```bash
cp .env.example .env
```

必要な環境変数：
- `OPENWEATHERMAP_API_KEY`: [OpenWeatherMap](https://openweathermap.org/api)のAPIキー
- `CHATWORK_API_TOKEN`: ChatWorkのAPIトークン
- `CHATWORK_ROOM_ID`: 通知先のChatWorkルームID

### 3. エージェントの実行

```bash
uv run adk src
```

このコマンドでADKサーバーが起動し、ブラウザでエージェントとの対話が可能になります。

## 使用例

### 基本的な天気情報取得
```
東京の天気を教えて
```

### ChatWorkへの天気情報送信
```
大阪の天気をChatWorkに送信して
```

### ルーム情報の確認
```
ChatWorkのルーム情報を確認して
```

## ツール詳細

### 天気情報ツール
- `get_weather(location)`: 都市名による天気情報取得
- `get_coordinates_from_city(city_name)`: 都市名から緯度経度を取得
- `get_weather_by_coordinates(lat, lon)`: 座標による天気情報取得

### ChatWorkツール
- `send_chatwork_message(room_id, message)`: メッセージ送信
- `get_room_info()`: 環境変数で設定されたルームの情報取得

## 技術スタック

- **フレームワーク**: Google ADK (Agent Development Kit)
- **API**: OpenWeatherMap API, ChatWork API
- **パッケージ管理**: uv
