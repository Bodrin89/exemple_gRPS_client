from fastapi import APIRouter
from google.protobuf.json_format import MessageToJson

from grpc_clients.auth_grpc_client import UnaryClient, ValidTokenClient
from src.schemas.auth_schemas import AuthIn, AuthOut, UpdateTokenIn

auth_router = APIRouter(prefix='/auth', tags=['auth'])


@auth_router.post('/jwt', response_model=AuthOut)
async def generate_jwt_token(auth_data: AuthIn):
    """View для получения access и refresh токенов"""
    auth_data_json = auth_data.json()
    client = UnaryClient()
    result = client.get_url(message=auth_data_json)
    json_response = MessageToJson(message=result, preserving_proto_field_name=True)
    return AuthOut.parse_raw(json_response)


@auth_router.post('/refresh', response_model=AuthOut)
async def refresh_jwt_token(refresh_token: UpdateTokenIn):
    """View для обновления access токена"""
    json_data = refresh_token.json()
    client = ValidTokenClient()
    result = client.get_url(message=json_data)
    json_response = MessageToJson(message=result, preserving_proto_field_name=True)
    return AuthOut.parse_raw(json_response)
