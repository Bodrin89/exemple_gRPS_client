from fastapi import APIRouter
from google.protobuf.json_format import MessageToJson

from grpc_client import UnaryClient
from src.schemas.auth_schemas import AuthIn, AuthOut

auth_router = APIRouter(prefix='/auth', tags=['auth'])


@auth_router.post('/jwt', response_model=AuthOut)
async def generate_jwt_token(auth_data: AuthIn):
    """View для получения access и refresh токенов"""
    auth_data_json = auth_data.json()
    client = UnaryClient()
    result = client.get_url(message=auth_data_json)
    json_response = MessageToJson(message=result, preserving_proto_field_name=True)
    return AuthOut.parse_raw(json_response)
