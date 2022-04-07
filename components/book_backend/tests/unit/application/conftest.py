from unittest.mock import Mock
import pytest
from book.application import dataclasses, interfaces


@pytest.fixture(scope='function')
def book():
    return dataclasses.Book(
        author='test_author',
        published_year=1899,
        title='test_title',
        id=1

    )


@pytest.fixture(scope='function')
def book_user():
    return dataclasses.Book(
        author='test_author',
        published_year=1899,
        title='test_title',
        id=1,
        user_id=1
    )


@pytest.fixture(scope='function')
def book_repo(book, book_user):
    book_repo = Mock(interfaces.BooksRepo)
    book_repo.get_by_id = Mock(return_value=book_user)
    book_repo.add_instance = Mock(return_value=book)
    book_repo.get_all = Mock(return_value=book)
    book_repo.delete_instance = Mock(return_value=book)
    book_repo.take_book = Mock(return_value=book)
    book_repo.return_book = Mock(return_value=book)
    return book_repo
