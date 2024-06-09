from fastapi import APIRouter, UploadFile, File, HTTPException, Query, Depends
from src.middleware.auth.auth import get_api_key
from src.shared.shared import summarize_model

router = APIRouter()


@router.post("/api/summarization", dependencies=[Depends(get_api_key)])
async def summarization(
    text: str,
    model_name: str = Query(None),
):
    summarizer = summarize_model(model_name)
    try:
        summary = await summarizer(text)
        return {"res": summary}

    except Exception as e:
        print("Something went wrong: ", e)
        return {"error": str(e)}
