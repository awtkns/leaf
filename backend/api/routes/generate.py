from fastapi import APIRouter
from api import db
from . import generate_helper

router = APIRouter()


@router.get('/')
async def return_acronyms():

    # TODO: delete demo payload below
    payload = {
        "acronym": "SFU",
        "words": ["Simon Fraser University", "Surprising Fantastic Upright", "Skilled Fortunate User", "Sad Frustrated Upset"]
    }

    return payload