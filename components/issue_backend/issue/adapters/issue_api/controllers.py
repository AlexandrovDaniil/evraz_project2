import json

import jwt

from issue.application import services
from classic.components import component
from classic.http_auth import authenticate, authenticator_needed

from .join_points import join_point


@component
class Issues:
    issues: services.Issues

    @join_point
    def on_get_show_all(self, request, response):
        issues = self.issues.get_all()
        response.media = [{
            'issue_id': issue.id,
            'book_id': issue.id_book,
            'user_id': issue.id_user,
            'action': issue.action,
            'date': issue.date
        } for issue in issues]

    @join_point
    def on_get_show_user(self, request, response):
        users = self.issues.get_user_action()
        response.media = [{
            'issue_id': user[0],
            'user_id': user[1],
            'action': user[2],
            'date': user[3]
        } for user in users]

    @join_point
    def on_get_show_book(self, request, response):
        books = self.issues.get_book_action()
        response.media = [{
            'issue_id': book[0],
            'book_id': book[1],
            'action': book[2],
            'date': book[3]
        } for book in books]