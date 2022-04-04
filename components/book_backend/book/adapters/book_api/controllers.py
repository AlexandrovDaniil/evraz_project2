from book.application import services
from classic.components import component

from .join_points import join_point


@component
class Books:
    books: services.Books

    @join_point
    def on_get_show_info(self, request, response):
        book = self.books.get_info(**request.params)
        response.media = {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'published_year': book.published_year

        }

    @join_point
    def on_post_add_book(self, request, response):
        self.books.add_book(**request.media)
        response.media = {'status': 'book added'}

    @join_point
    def on_get_show_all(self, request, response):
        books = self.books.get_all()
        response.media = {book[0]: book[3] for book in books}

    @join_point
    def on_get_delete_book(self, request, response):
        self.books.delete_book(**request.params)
        response.media = {'status': 'book deleted'}
