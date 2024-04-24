import grpc
from fastapi import HTTPException

import protobuf.get_user_info_pb2 as get_user_info_pb2
import protobuf.get_user_info_pb2_grpc as get_user_info_pb2_grpc
import protobuf.update_token.update_token_pb2 as update_token_pb2
import protobuf.update_token.update_token_pb2_grpc as update_token_pb2_grpc
from src.config.settings import GRPC_HOST, GRPC_PORT


class UnaryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = GRPC_HOST
        self.server_port = GRPC_PORT

        # instantiate a channel
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = get_user_info_pb2_grpc.UnaryStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """

        message = get_user_info_pb2.Message(message=message)
        try:
            result = self.stub.GetServerResponse(message)
            return result
        except grpc.RpcError as e:
            details = e.args[0].details
            raise HTTPException(status_code=401, detail=details)


class ValidTokenClient(object):
    def __init__(self):
        self.host = GRPC_HOST
        self.server_port = GRPC_PORT
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.server_port))
        self.stub = update_token_pb2_grpc.ValidTokenStub(self.channel)

    def get_url(self, message):
        message = update_token_pb2.Message(message=message)

        try:
            result = self.stub.GetServerResponse(message)
            return result
        except grpc.RpcError as e:
            details = e.args[0].details
            raise HTTPException(status_code=401, detail=details)
