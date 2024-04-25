from fastapi import FastAPI

from src.config.tortoise_connection import connect_db
from src.view.auth_view import auth_router
from src.view.film_view import film_router

app = FastAPI(title='Auth Service', debug=True)

app.include_router(auth_router)
app.include_router(film_router)

connect_db(app)
