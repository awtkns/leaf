from fastapi import APIRouter
from api import db
from . import generate_helper

router = APIRouter()


@router.get('/')
async def return_acronyms():

    valid_pair = generate_helper.build_valid_pair()

    # TODO: delete dummy list
    random_phrases = ['decoy_1','decoy_2','decoy_3']
    
    generate_helper.build_payload(valid_pair, random_phrases)

    return valid_pair