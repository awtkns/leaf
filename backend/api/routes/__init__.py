from api import app
from . import ping
from . import generate

# Secure Routes
app.include_router(ping.router, tags=['Ping Pong'], prefix='/ping')
app.include_router(generate.router, tags=['Generate Acronyms'], prefix='/generate')
