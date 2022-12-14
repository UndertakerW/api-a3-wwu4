from concurrent import futures
import logging

import os, sys

import grpc
import inventoryService_pb2
import inventoryService_pb2_grpc

# Approach to store data: dictionary with hardcoded data
# Please see db.py for more details
import db


class InventoryService(inventoryService_pb2_grpc.InventoryServiceServicer):

    # Create a book in the inventory
    # request contains:
    # Book book = 1
    def CreateBook(self, request, context):

        # Check the mandatory field book.isbn

        if request.book is None:
            return inventoryService_pb2.CreateBookResponse(
                status=inventoryService_pb2.ServiceStatus.SERVICE_ISBN_ERROR,
                message='[Error] Mandatory field ISBN is missing.'
            )

        if request.book.isbn is None or len(request.book.isbn) == 0:
            return inventoryService_pb2.CreateBookResponse(
                status=inventoryService_pb2.ServiceStatus.SERVICE_ISBN_ERROR,
                message='[Error] Mandatory field ISBN is missing.'
            )

        if request.book.isbn in db.books:
            return inventoryService_pb2.CreateBookResponse(
                status=inventoryService_pb2.ServiceStatus.SERVICE_ISBN_ERROR,
                message='[Error] Book with ISBN %s exists.' % request.book.isbn
            )

        # Create a new BookObject and add it to the database
        newBook = db.BookObject()
        newBook.isbn = request.book.isbn
        newBook.year = request.book.year
        newBook.author = request.book.author
        newBook.genre = request.book.genre
        newBook.title = request.book.title
        db.books[request.book.isbn] = newBook

        # Return status and message
        return inventoryService_pb2.CreateBookResponse(
            status=inventoryService_pb2.ServiceStatus.SERVICE_SUCCESS,
            message='Book with ISBN %s created successfully.' % request.book.isbn
        )

    # Create a book in the inventory
    # request contains:
    # string isbn = 1
    def GetBook(self, request, context):

        # Check the mandatory field isbn

        if request.isbn is None or len(request.isbn) == 0:
            return inventoryService_pb2.GetBookResponse(
                status=inventoryService_pb2.ServiceStatus.SERVICE_ISBN_ERROR,
                message='[Error] Mandatory field ISBN is missing.'
            )

        if request.isbn not in db.books:
            return inventoryService_pb2.GetBookResponse(
                status=inventoryService_pb2.ServiceStatus.SERVICE_ISBN_ERROR,
                message='[Error] Book with ISBN %s does not exist.' % request.isbn
            )

        # Get the BookObject from database
        bookObject = db.books[request.isbn]

        # Craft a Book for proto
        book = inventoryService_pb2.book__pb2.Book(
            isbn=request.isbn,
            title=bookObject.title,
            author=bookObject.author,
            year=bookObject.year,
            genre=bookObject.genre
        )

        # Return status, message, and the Book
        return inventoryService_pb2.GetBookResponse(
            status=inventoryService_pb2.ServiceStatus.SERVICE_SUCCESS,
            message='Book with ISBN %s returned successfully.' % request.isbn,
            book=book
        )

# Start the server
def startServer(port):
    # Instantiate the server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Add the service
    inventoryService_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    # Set up the port
    server.add_insecure_port('[::]:' + str(port))
    # Start the server
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    if len(sys.argv) == 2:
        startServer(sys.argv[2])
    else:
        # Default port = 50051
        startServer(50051)
