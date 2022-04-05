from typing import Optional, List


from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from pydantic import validate_arguments

from . import errors, interfaces
from .dataclasses import Book

join_points = PointCut()
join_point = join_points.join_point


class BookInfo(DTO):
    author: str
    published_year: int
    title: str
    id: Optional[int]
    status: Optional[str]

@component
class Books:
    book_repo: interfaces.BooksRepo

    @join_point
    @validate_arguments
    def get_info(self, id: int):
        book = self.book_repo.get_by_id(id)
        if not book:
            raise errors.NoBook(id=id)
        return book

    @join_point
    @validate_with_dto
    def add_book(self, book_info: BookInfo):
        new_book = book_info.create_obj(Book)
        self.book_repo.add_instance(new_book)

    @join_point
    @validate_arguments
    def delete_book(self, id: int):
        book = self.book_repo.get_by_id(id)
        if not book:
            raise errors.NoBook(id=id)
        self.book_repo.delete_instance(id)

    @join_point
    def get_all(self) -> List[Book]:
        books = self.book_repo.get_all()
        return books

    @join_point
    @validate_arguments
    def change_book_status(self, id: int):
        book = self.book_repo.get_by_id(id)
        if not book:
            raise errors.NoBook(id=id)
        self.book_repo.change_status(id)

