from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def ping_pong():
    return 'Pong'
