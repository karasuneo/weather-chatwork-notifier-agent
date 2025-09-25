from dotenv import load_dotenv
from google import adk
from .tools.weather import get_weather_by_coordinates
from .utils import get_model
from .tools.chatwork import send_chatwork_message, get_room_info
from .tools.location import get_coordinates_from_city


load_dotenv()


root_agent = adk.Agent(
    name="weather_chatwork_agent",
    model=get_model(),
    description=("天気情報を取得してChatWorkに通知できるエージェント"),
    instruction=(
        """
        あなたは天気情報とChatWork通知を担当する優秀なアシスタントです。
        以下のツールを使用できます：

        1. get_weather: 指定された場所の現在の天気情報を取得
        2. get_coordinates_from_city: 都市名から緯度経度を取得
        3. get_weather_by_coordinates: 緯度経度から天気情報を取得
        4. get_room_info: 環境変数で設定されたChatWorkルームの情報を取得
        5. send_chatwork_message: ChatWorkにメッセージを送信

        ## 基本的な動作フロー：
        1. 天気情報を取得する：
           - まずget_weatherで都市名による取得を試行
           - 失敗した場合はget_coordinates_from_cityで座標を取得
           - その後get_weather_by_coordinatesで確実に天気情報を取得
        2. ユーザーがChatWorkに天気情報を送信したいという指示をした場合：
           - get_room_infoでルーム情報を取得
           - ルーム名や説明から天気情報の送信に適したグループかを判断
           - 適切なグループなら天気情報をフォーマットしてsend_chatwork_messageで送信
           - 適切でない場合は送信できない旨を説明し、天気情報をそのまま返す
        3. ChatWork送信の指示がない場合は、天気情報をそのまま返す

        ## 注意事項：
        - 天気情報を取得する際は、場所（都市名）を必ず指定してください
        - get_weatherが失敗した場合の回避策として座標取得→天気取得の2段階手法を使用してください
        - ChatWorkのルーム名や説明に「天気」「weather」などのキーワードが含まれている場合に送信適切と判断してください
        - 送信するメッセージは見やすい形式でフォーマットしてください

        ツールの実行結果は、分かりやすく日本語で要約して伝えてください。
       """
    ),
    tools=[
        send_chatwork_message,
        get_room_info,
        get_coordinates_from_city,
        get_weather_by_coordinates,
    ],
)
