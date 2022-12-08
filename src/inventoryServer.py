from concurrent import futures
import logging

import os, sys
# getting the name of the directory
# where this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)

import grpc
import service.book_pb2
import service.inventoryItem_pb2
import service.inventoryService_pb2
import service.inventoryService_pb2_grpc

class InventoryService(service.inventoryService_pb2_grpc.InventoryServiceServicer):

    def CreateBook(self, request, context):
        return service.inventoryService_pb2.CreateBookResponse(
            status=service.inventoryService_pb2.CreateBookStatus.SUCCESS,
            message='Book with ISBN %s created successfully.' % request.book.isbn
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service.inventoryService_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()