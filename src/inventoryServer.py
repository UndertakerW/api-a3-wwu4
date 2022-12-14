from concurrent import futures
import logging

import os, sys


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import grpc
import service.inventoryService_pb2
import service.inventoryService_pb2_grpc

# Approach to store data: dictionary with hardcoded data
# Please see db.py for more details
import db

port = 50051

class InventoryService(service.inventoryService_pb2_grpc.InventoryServiceServicer):

    def CreateBook(self, request, context):

        # Check the mandatory field isbn

        if request.book is None:
            return service.inventoryService_pb2.CreateBookResponse(
                status=service.inventoryService_pb2.ServiceStatus.SERVICE_ISBN_ERROR,
                message='[Error] Mandatory field ISBN is missing.'
            )

        if request.book.isbn is None or len(request.book.isbn) == 0:
            return service.inventoryService_pb2.CreateBookResponse(
                status=service.inventoryService_pb2.ServiceStatus.SERVICE_ISBN_ERROR,
                message='[Error] Mandatory field ISBN is missing.'
            )

        if request.book.isbn in db.books:
            return service.inventoryService_pb2.CreateBookResponse(
                status=service.inventoryService_pb2.ServiceStatus.SERVICE_ISBN_ERROR,
                message='[Error] Book with ISBN %s exists.' % request.book.isbn
            )

        newBook = db.BookObject()
        newBook.isbn = request.book.isbn
        newBook.year = request.book.year
        newBook.author = request.book.author
        newBook.genre = request.book.genre
        newBook.title = request.book.title
        db.books[request.book.isbn] = newBook

        # print(db.books[request.book.isbn])

        return service.inventoryService_pb2.CreateBookResponse(
            status=service.inventoryService_pb2.ServiceStatus.SERVICE_SUCCESS,
            message='Book with ISBN %s created successfully.' % request.book.isbn
        )

    def GetBook(self, request, context):

        if request.isbn is None or len(request.isbn) == 0:
            return service.inventoryService_pb2.GetBookResponse(
                status=service.inventoryService_pb2.ServiceStatus.SERVICE_ISBN_ERROR,
                message='[Error] Mandatory field ISBN is missing.'
            )

        if request.isbn not in db.books:
            return service.inventoryService_pb2.GetBookResponse(
                status=service.inventoryService_pb2.ServiceStatus.SERVICE_ISBN_ERROR,
                message='[Error] Book with ISBN %s does not exist.' % request.isbn
            )

        book = service.inventoryService_pb2.book__pb2.Book(
            isbn=request.isbn,
            title=db.books[request.isbn].title,
            author=db.books[request.isbn].author,
            year=db.books[request.isbn].year,
            genre=db.books[request.isbn].genre
        )

        return service.inventoryService_pb2.GetBookResponse(
            status=service.inventoryService_pb2.ServiceStatus.SERVICE_SUCCESS,
            message='Book with ISBN %s returned successfully.' % request.isbn,
            book=book
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service.inventoryService_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:'+str(port))
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
