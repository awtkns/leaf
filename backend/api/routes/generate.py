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

    phrases = ["", "", ""]
    for c in acronym:
        words = []
        
        async for wordData in db.client.unigrams.get_collection(c.lower()).find():
            words.append(wordData['word'])
        
        for i in range(3):
            phrases[i] += random.choice(words) + " "
    
    return phrases


@router.get('/')
async def return_acronyms():
    valid_pair = generate_helper.build_valid_pair()

    # TODO: delete dummy list
    random_phrases = ['decoy_1','decoy_2','decoy_3']
    
    generate_helper.build_payload(valid_pair, random_phrases)

    return valid_pair