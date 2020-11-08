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
async def return_acronyms():
    valid_pair = generate_helper.build_valid_pair()

    # TODO: delete dummy list
    random_phrases = ['decoy_1','decoy_2','decoy_3']

    generate_helper.build_payload(valid_pair, random_phrases)
    print(valid_pair)

    return valid_pair