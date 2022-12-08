# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import inventoryService_pb2 as inventoryService__pb2


class InventoryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateBook = channel.unary_unary(
                '/InventoryService/CreateBook',
                request_serializer=inventoryService__pb2.CreateBookRequest.SerializeToString,
                response_deserializer=inventoryService__pb2.CreateBookResponse.FromString,
                )
        self.GetBook = channel.unary_unary(
                '/InventoryService/GetBook',
                request_serializer=inventoryService__pb2.GetBookRequest.SerializeToString,
                response_deserializer=inventoryService__pb2.GetBookResponse.FromString,
                )


class InventoryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateBook(self, request, context):
        """a. CreateBook - self-explanatory
        Hint: think of a response format that doesn’t include an object
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBook(self, request, context):
        """b. GetBook - given ISBN, retrieve book details
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InventoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateBook': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBook,
                    request_deserializer=inventoryService__pb2.CreateBookRequest.FromString,
                    response_serializer=inventoryService__pb2.CreateBookResponse.SerializeToString,
            ),
            'GetBook': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBook,
                    request_deserializer=inventoryService__pb2.GetBookRequest.FromString,
                    response_serializer=inventoryService__pb2.GetBookResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'InventoryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InventoryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/CreateBook',
            inventoryService__pb2.CreateBookRequest.SerializeToString,
            inventoryService__pb2.CreateBookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/GetBook',
            inventoryService__pb2.GetBookRequest.SerializeToString,
            inventoryService__pb2.GetBookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
