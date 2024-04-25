import grpc
from fastapi import HTTPException

import protobuf.get_role_user.get_role_pb2 as get_role_pb2
import protobuf.get_role_user.get_role_pb2_grpc as get_role_pb2_grpc
from src.config.settings import GRPC_HOST, GRPC_PORT


class FilmGrpcClient(object):
    def __init__(self):
        self.host = GRPC_HOST
        self.port = GRPC_PORT
        self.channel = grpc.insecure_channel(f'{self.host}:{self.port}')
        self.stub = get_role_pb2_grpc.GetRoleStub(self.channel)

    def get_server_response(self, token):
        token = get_role_pb2.Token(access_token=token)
        try:
            result = self.stub.GetServerResponse(token)
            return result
        except grpc.RpcError as e:
            details = e.args[0].details
            raise HTTPException(status_code=401, detail=details)
