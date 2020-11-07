from api import app
from . import generate

# Secure Routes
app.include_router(generate.router, tags=['Generate Acronyms'], prefix='/generate')
