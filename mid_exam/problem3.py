def add_book_func(data, book):
    if book not in data:
        data.insert(0, book)
        return data


def take_book_func(data, book):
    if book in data:
        data.remove(book)
        return data


def swap_books_func(data, book, second_book):
    books = book.split(" | ")
    book1 = books[0]
    book2 = books[1]

    a, b = data.index(book1), data.index(book2)
    data[a], data[b] = data[b], data[a]

    return data


def insert_book_func(data, book):
    if book not in data:
        data.append(book)
        return data

def check_book_func(data, book):
    return data


def book_shelve(data):

    while True:
        command = input().split(" | ")

        if command[0] == "Done":
            print(", ".join(data))
            break

        current_command = command[0]
        book = command[1]

        if current_command == "Add Book":
            data = add_book_func(data, book)

        elif current_command == "Take Book":
            data = take_book_func(data, book)

        elif current_command == "Swap Books":
            data = swap_books_func(data, book)

        elif current_command == "Insert Book":
            data = insert_book_func(data, book)

        elif current_command == "Check Book":
            data = check_book_func(data, book)


books = input().split("&")
book_shelve(books)