from fastapi import APIRouter
from api import db

router = APIRouter()


@router.get('/')
async def ping_pong():
    await db.client.pings.get_collection('pings').insert_one({'ping':'pong'})
    pongs = []

    async for pong in db.client.pings.get_collection('pings').find():
        pongs.append(pong['ping'])

    return {'pings': pongs}
