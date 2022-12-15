import inventory_client


def get_titles(client, isbns):
    titles = []
    for isbn in isbns:
        status, message, book = client.get_book_from_server(isbn)
        # Return title if found
        if book:
            titles.append(book.title)
        # Return message if not found
        else:
            titles.append(message)
    return titles


if __name__ == '__main__':
    # i. create an instance of client api object with reasonable defaults to access the server
    client = inventory_client.InventoryClient('::', '50051')
    # ii. call the defined function using two hardcoded ISBNs as a parameter
    isbns = ['978–0–07–340320–5', '978-0-470-01270-3']
    titles = get_titles(client, isbns)
    # iii. print returned titles to standard output
    print(titles)
