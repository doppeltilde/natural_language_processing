from fastapi import APIRouter, Query, Depends
from src.middleware.auth.auth import get_api_key
from src.shared.shared import summarization_model
import time
import torch

router = APIRouter()


@router.post("/api/summarization", dependencies=[Depends(get_api_key)])
async def summarization(
    text: str,
    model_name: str = Query(None),
):
    start_time = time.time()
    summarizer = summarization_model(model_name)
    try:
        summary = summarizer(text)
        return {
            "execution_time": time.time() - start_time,
            "res": summary,
        }

    except Exception as e:
        print("Something went wrong: ", e)
        return {"error": str(e)}

    finally:
        del summarizer
        torch.cuda.empty_cache()
