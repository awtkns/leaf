import random
import string
from pydantic import BaseModel

from fastapi import APIRouter
from api import db
from . import generate_helper

router = APIRouter()


@router.get('/single')
async def get_single_meaning(acronym: str = 'SFU'):
    """ Returns a single word corresponding to and acronym"""

    words = ["Simon Fraser University", "Surprising Fantastic Upright",
        "Skilled Fortunate User", "Sad Frustrated Upset"]

    return random.choice(words)


@router.get('/')
async def return_acronyms(acronym: str = 'SFU'):
    # TODO: delete demo payload below
	randomVal = random.randint(10, 15)
	payload = {
        "acronym": "SFU",
        "words": ["Simon Fraser University", "Surprising Fantastic Upright", "Skilled Fortunate User", str(randomVal)]
    }
	
	return payload
