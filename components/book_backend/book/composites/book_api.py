from book.adapters import book_api, database
from book.application import services
from classic.sql_storage import TransactionContext
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Settings:
    db = database.Settings()
    book_api = book_api.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL, echo=True)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)
    Session = sessionmaker(bind=engine)
    books_repo = database.repositories.BooksRepo(context=context)


class Application:
    is_dev_mode = Settings.book_api.IS_DEV_MODE
    books = services.Books(book_repo=DB.books_repo)


class Aspects:
    services.join_points.join(DB.context)
    book_api.join_points.join(DB.context)


app = book_api.create_app(
    is_dev_mode=Application.is_dev_mode,
    books=Application.books,

)
