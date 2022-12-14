import grpc
import os, sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import service.inventoryService_pb2
import service.inventoryService_pb2_grpc
import service.inventoryServer


class InventoryClient:
    def __init__(self, address, port):
        endpoint = '[{address}]:{port}'.format(address=address, port=port)
        channel = grpc.insecure_channel(endpoint)
        self.stub = service.inventoryService_pb2_grpc.InventoryServiceStub(channel)

    # Get a book from the server using isbn
    # param: (string) isbn, isbn of a book
    # return: (int) status
    #         (string) message
    #         (Book) book, the book fetched from the server if successful
    def getBookFromServer(self, isbn):
        request = service.inventoryService_pb2.GetBookRequest(isbn=isbn)
        response = self.stub.GetBook(request)
        # Return book if successful
        if response.status == service.inventoryService_pb2.ServiceStatus.SERVICE_SUCCESS:
            return response.status, response.message, response.book
        # Return None if failed
        else:
            return response.status, response.message, None
