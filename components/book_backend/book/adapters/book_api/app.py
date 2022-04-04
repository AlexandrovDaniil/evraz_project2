from book.application import services
from classic.http_api import App

from . import auth, controllers


def create_app(
        is_dev_mode: bool,
        books: services.Books,
) -> App:
    app = App(prefix='/api')
    app.register(controllers.Books(books=books))
    return app
