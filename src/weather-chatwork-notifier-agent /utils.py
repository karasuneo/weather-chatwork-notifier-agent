import os
from google.adk.models.lite_llm import LiteLlm


def get_model():
    return LiteLlm(
        model=os.getenv("COMPLETION_MODEL"),
    )
