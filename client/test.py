import unittest
import get_book_titles


class TestGetBookTitles(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        # Init the super class
        super(TestGetBookTitles, self).__init__(*args, **kwargs)

    # Test get_book_titles.getTitles() with a Mock of API class interface
    def getTitlesFromMockTest(self):
        # Create Mock
        client = unittest.Mock()

        isbns = ['978–0–07–340320–5', '978-0-470-01270-3']
        expected = ['Leadership Communication', 'Requirements Engineering']

        def side_effect(isbns):
            return expected

        client.getTitles.side_effect = side_effect

        actual = get_book_titles.getTitles(client, isbns)

        self.assertEqual(expected, actual)
