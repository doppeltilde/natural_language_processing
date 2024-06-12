from fastapi import APIRouter, Query, Depends
from src.middleware.auth.auth import get_api_key
from src.shared.shared import text_classification_model
import time
import torch

router = APIRouter()


@router.post("/api/text-classification", dependencies=[Depends(get_api_key)])
async def text_classification(
    text: str,
    model_name: str = Query(None),
):
    start_time = time.time()
    text_classifier = text_classification_model(model_name)
    try:
        response = text_classifier(text)
        return {
            "execution_time": time.time() - start_time,
            "res": response,
        }

    except Exception as e:
        print("Something went wrong: ", e)
        return {"error": str(e)}

    finally:
        del text_classifier
        torch.cuda.empty_cache()
