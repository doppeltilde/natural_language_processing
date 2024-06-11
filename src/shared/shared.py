from dotenv import load_dotenv
import os
from transformers import pipeline
import torch

load_dotenv()

access_token = os.getenv("ACCESS_TOKEN", None)

default_summarization_model_name = os.getenv(
    "DEFAULT_SUMMARIZATION_MODEL_NAME", "Falconsai/text_summarization"
)
default_translation_model_name = os.getenv(
    "DEFAULT_TRANSLATION_MODEL_NAME", "google-t5/t5-base"
)

device = 0 if torch.cuda.is_available() else -1

# API KEY
api_keys_str = os.getenv("API_KEYS", "")
api_keys = api_keys_str.split(",") if api_keys_str else []
use_api_keys = os.getenv("USE_API_KEYS", "False").lower() in ["true", "1", "yes"]


def summarization_model(model_name):
    try:
        _model_name = model_name or default_summarization_model_name

        summarizer = pipeline(
            "summarization",
            model=_model_name,
            device=device,
        )

        return summarizer

    except Exception as e:
        print(e)
        return {"error": str(e)}


def translation_model(model_name, input_language, output_language):
    try:
        _model_name = model_name or default_translation_model_name
        task_name = f"translation_{input_language}_to_{output_language}"

        translator = pipeline(
            task_name,
            model=_model_name,
            device=device,
        )

        return translator
    except Exception as e:
        print(e)
        return {"error": str(e)}
