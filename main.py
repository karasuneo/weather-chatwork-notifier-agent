import os
from datetime import datetime
from dotenv import load_dotenv
from google import adk
from google.adk.models.lite_llm import LiteLlm


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
    name="現在時刻通知エージェント",
    model=get_model(),
    description=("現在時刻通知ができるとてもとても優秀なエージェント"),
    instruction=(
        """
        あなたはとてもとても優秀なアシスタントです
        必要に応じて、現在時刻通知ツールを使って、現在の日時を取得してください
        ツールを呼び出した場合は、ツールの実行が成功したかを通知するため猫になってください
       """
    ),
    tools=[get_time],
)
