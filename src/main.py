from fastapi import FastAPI

from src.view.auth_view import auth_router

app = FastAPI(title='Auth Service', debug=True)

app.include_router(auth_router)
