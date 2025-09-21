import os
from datetime import datetime
from dotenv import load_dotenv
from google import adk
from google.adk.models.lite_llm import LiteLlm
from tools.weather import get_weather


load_dotenv()


# 共通のモデル設定
def get_model():
    return LiteLlm(
        model=os.getenv(
            "COMPLETION_MODEL", "bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0"
        ),
    )


def get_time() -> dict:
    """現在時刻を取得する関数"""
    return {"status": "success", "report": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


root_agent = adk.Agent(
    name="天気＆時刻通知エージェント",
    model=get_model(),
    description=("天気情報と現在時刻を通知できるとても優秀なエージェント"),
    instruction=(
        """
        あなたはとても優秀なアシスタントです。
        以下のツールを使用できます：

        1. get_time: 現在の日時を取得
        2. get_weather: 指定された場所の現在の天気情報を取得

        ユーザーの要求に応じて適切なツールを選択して使用してください。
        天気情報を取得する際は、場所（都市名）を必ず指定してください。

        ツールの実行結果は、分かりやすく日本語で要約して伝えてください。
       """
    ),
    tools=[get_time, get_weather],
)
