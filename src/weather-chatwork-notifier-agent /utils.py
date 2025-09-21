

def get_model():
    return LiteLlm(
        model=os.getenv(
            "COMPLETION_MODEL", "bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0"
        ),
    )