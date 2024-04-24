import grpc
from fastapi import HTTPException

import protobuf.get_user_info_pb2 as pb2
import protobuf.get_user_info_pb2_grpc as pb2_grpc


class UnaryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.UnaryStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Message(message=message)
        try:
            result = self.stub.GetServerResponse(message)
            return result
        except grpc.RpcError as e:
            details = e.args[0].details
            raise HTTPException(status_code=401, detail=details)
