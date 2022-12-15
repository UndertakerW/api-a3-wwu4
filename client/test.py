import os
import sys
import unittest
import unittest.mock

import get_book_titles
import inventory_client

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import service.inventoryService_pb2


TEST_SERVER = True

def set_up_mock():
    # Create mock API client
    client = unittest.mock.Mock()

    # Define mock behavior

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
            return service.inventoryService_pb2.ServiceStatus.SERVICE_SUCCESS,\
                    'Book with ISBN 978–0–07–340320–5 returned successfully.',\
                    book1
        elif isbn == '978-0-470-01270-3':
            return service.inventoryService_pb2.ServiceStatus.SERVICE_SUCCESS,\
                    'Book with ISBN 978-0-470-01270-3 returned successfully.',\
                    book2
        else:
            return service.inventoryService_pb2.ServiceStatus.SERVICE_ISBN_ERROR,\
                    '[Error] Book with this ISBN does not exist.',\
                    None

    client.get_book_from_server.side_effect = side_effect

    return client


class TestGetBookTitles(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        # Init the super class
        super(TestGetBookTitles, self).__init__(*args, **kwargs)

    # Test get_book_titles.getTitles() with a mock client
    def test_get_titles_from_mock(self):
        # Create Mock
        client = set_up_mock()

        # Prepare test data
        isbns = ['978–0–07–340320–5', '978-0-470-01270-3']
        expected = ['Leadership Communication', 'Requirements Engineering']

        # Pass the newly created mock object as a client API accessor
        actual = get_book_titles.get_titles(client, isbns)

        self.assertEqual(expected, actual)


    # Test get_book_titles.getTitles() with a mock client
    # Mock ISBN not found
    def test_get_titles_from_mock_isbn_not_found(self):
        # Create Mock
        client = set_up_mock()

        # Prepare test data
        isbns = ['invalid_isbn_1', 'invalid_isbn_2']
        expected = ['[Error] Book with this ISBN does not exist.',
                    '[Error] Book with this ISBN does not exist.']

        # Pass the newly created mock object as a client API accessor
        actual = get_book_titles.get_titles(client, isbns)

        self.assertEqual(expected, actual)

    # Test get_book_titles.getTitles() with a live server
    @unittest.skipUnless(TEST_SERVER, 'Test with server')
    def test_get_titles_from_server(self):
        # Instantiate client
        client = inventory_client.InventoryClient('::', '50051')

        # Prepare test data
        isbns = ['978–0–07–340320–5', '978-0-470-01270-3']
        expected = ['Leadership Communication', 'Requirements Engineering']

        # Get data using client
        actual = get_book_titles.get_titles(client, isbns)

        self.assertEqual(expected, actual)

    # Test get_book_titles.getTitles() with a live server
    # Test ISBN not found
    @unittest.skipUnless(TEST_SERVER, 'Test with server')
    def test_get_titles_from_server_isbn_not_found(self):
        # Instantiate client
        client = inventory_client.InventoryClient('::', '50051')

        # Prepare test data
        isbns = ['invalid_isbn_1', 'invalid_isbn_2']
        expected = ['[Error] Book with ISBN invalid_isbn_1 does not exist.',
                    '[Error] Book with ISBN invalid_isbn_2 does not exist.']

        # Get data using client
        actual = get_book_titles.get_titles(client, isbns)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()