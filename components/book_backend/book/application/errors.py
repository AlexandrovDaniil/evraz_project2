from classic.app.errors import AppError


class NoBook(AppError):
    msg_template = "No book with id '{id}'"
    code = 'chat.no_book'
