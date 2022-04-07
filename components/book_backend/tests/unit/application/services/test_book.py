import pytest
from attr import asdict
from book.application.services import Books
from book.application.errors import NotAvailable, WrongUser
from pydantic import ValidationError


@pytest.fixture(scope='function')
def service_book(book_repo):
    return Books(book_repo=book_repo)


data_book = {
    'author': 'test_author',
    'published_year': 1899,
    'title': 'test_title',
    'id': 1,
    'user_id': None
}

data_book_user = {
    'author': 'test_author',
    'published_year': 1899,
    'title': 'test_title',
    'id': 1,
    'user_id': 1
}


def test_add_book(service_book):
    service_book.add_book(**data_book)
    service_book.book_repo.add_instance.assert_called_once()


def test_get_book(service_book):
    book = service_book.get_info(id=1)
    assert asdict(book) == data_book_user


def test_get_book_missing_id(service_book):
    with pytest.raises(ValidationError):
        service_book.get_info()


def test_get_all(service_book):
    book = service_book.get_all()
    assert asdict(book) == data_book


def test_delete_book(service_book):
    service_book.delete_book(id=1)
    service_book.book_repo.delete_instance.assert_called_once()


def test_take_book_not_available(service_book):
    with pytest.raises(NotAvailable):
        service_book.take_book(user_id=2, book_id=1)


def test_return_book_wrong_user(service_book):
    with pytest.raises(WrongUser):
        service_book.return_book(user_id=2, book_id=1)


def test_return_book(service_book):
    service_book.return_book(user_id=1, book_id=1)
    service_book.book_repo.return_book.assert_called_once()
