from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware


from motor.motor_asyncio import AsyncIOMotorClient
from config import BaseConfig
config = BaseConfig()

app = FastAPI(docs_url='/', title='FallHack 2020 Api')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from .database import db

app.add_event_handler("startup", db.connect)
app.add_event_handler("shutdown", db.disconnect)

from . import routes

from . import sockets
app.mount('/ws', sockets.sio_app)