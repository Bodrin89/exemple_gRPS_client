from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from grpc_clients.film_grpc_client import FilmGrpcClient
from src.schemas.film_schemas import FilmCreateIn, FilmSchemaOut
from src.services.film_services import FilmServices

film_router = APIRouter(prefix='/films', tags=['films'])


@film_router.post('/create-films', response_model=FilmSchemaOut)
async def get_films(body: FilmCreateIn, credentials_token: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    """View для создания фильмов"""
    token = credentials_token.credentials
    client = FilmGrpcClient()
    result = client.get_server_response(token=token)
    role = result.role.lower()
    if role == 'admin':
        return await FilmServices.create_film(body)
    raise HTTPException(status_code=403, detail='У вас нет прав для создания фильмов')
