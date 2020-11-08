import random
import string
from pydantic import BaseModel

from fastapi import APIRouter
from api import db
from . import generate_helper

router = APIRouter()


@router.get('/single')
async def get_single_meaning(acronym: str = 'SFU'):
    """ Returns a single phrase corresponding to an acronym"""

    return await generate_helper.generate_random_acronyms(acronym = acronym, numPhrases = 1)

@router.get('/')
async def return_acronyms():
    valid_pair = generate_helper.build_valid_pair()
    random_phrases = await generate_helper.generate_random_acronyms(acronym = valid_pair['acron'], numPhrases = 3)
    generate_helper.build_payload(valid_pair, random_phrases)

    return valid_pair