from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware


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

from . import routes
