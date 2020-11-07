from api import app
from . import ping

# Secure Routes
app.include_router(ping.router, tags=['Ping Pong'], prefix='/ping')
