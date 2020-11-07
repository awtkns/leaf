from api import app
from . import ping
from . import sockets

# Secure Routes
app.include_router(ping.router, tags=['Ping Pong'], prefix='/ping')

# Mount socket
app.mount('/ws', sockets.sio_app)