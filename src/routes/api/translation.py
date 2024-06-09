from fastapi import APIRouter, Query, Depends
from src.middleware.auth.auth import get_api_key
from src.shared.shared import translation_model

router = APIRouter()


@router.post("/api/translation", dependencies=[Depends(get_api_key)])
async def translation(
    text: str,
    model_name: str = Query(None),
    input_language: str = Query("en", description="Input language"),
    output_language: str = Query("de", description="Output language"),
):
    translator = translation_model(model_name, input_language, output_language)

    try:
        translation = translator(text)
        return {"res": translation}

    except Exception as e:
        print("Something went wrong: ", e)
        return {"error": str(e)}
