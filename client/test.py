import os
import sys
import unittest
import unittest.mock

import get_book_titles

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import service.inventoryService_pb2

class TestGetBookTitles(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        # Init the super class
        super(TestGetBookTitles, self).__init__(*args, **kwargs)

    # Test get_book_titles.getTitles() with a Mock of API class interface
    def test_getTitlesFromMock(self):
        # Create Mock
        client = unittest.mock.Mock()

        isbns = ['978–0–07–340320–5', '978-0-470-01270-3']
        expected = ['Leadership Communication', 'Requirements Engineering']

        book1 = service.inventoryService_pb2.book__pb2.Book(
            isbn='978–0–07–340320–5',
            title='Leadership Communication',
            author='Deborah J. Barrett',
            year=2014,
            genre=1
        )

        book2 = service.inventoryService_pb2.book__pb2.Book(
            isbn='978-0-470-01270-3',
            title='Requirements Engineering',
            author='Axel van Lamsweerde',
            year=2009,
            genre=2
        )

        def side_effect(isbn):
            if isbn == '978–0–07–340320–5':
                return service.inventoryService_pb2.ServiceStatus.SERVICE_SUCCES,\
                        'Book with ISBN 978–0–07–340320–5 returned successfully.',\
                        book1
            elif isbn == '978-0-470-01270-3':
                return service.inventoryService_pb2.ServiceStatus.SERVICE_SUCCES,\
                        'Book with ISBN 978-0-470-01270-3 returned successfully.',\
                        book2

        client.getTitles.side_effect = side_effect

        status, message, actual = get_book_titles.getTitles(client, isbns)

        self.assertEqual(expected, actual)
