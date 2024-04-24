from fastapi import FastAPI
from google.protobuf.json_format import MessageToJson

from grpc_client import UnaryClient
from src.schemas.auth_schemas import AuthIn, AuthOut

app = FastAPI()


@app.post('/auth', response_model=AuthOut)
async def get_jwt_token(auth_data: AuthIn):
    auth_data_json = auth_data.json()
    client = UnaryClient()
    result = client.get_url(message=auth_data_json)
    json_response = MessageToJson(message=result, preserving_proto_field_name=True)
    return AuthOut.parse_raw(json_response)
