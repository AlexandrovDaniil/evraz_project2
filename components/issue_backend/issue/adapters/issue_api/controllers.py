from issue.application import services
from classic.components import component
from classic.http_auth import authenticate, authenticator_needed

from .join_points import join_point


@authenticator_needed
@component
class Issues:
    issues: services.Issues

    @join_point
    @authenticate
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
    @authenticate
    def on_get_show_all_by_user(self, request, response):
        request.params['user_id'] = request.context.client.user_id
        issues = self.issues.get_all_by_user(**request.params)
        response.media = [{
            'issue_id': issue.id,
            'book_id': issue.id_book,
            'user_id': issue.id_user,
            'action': issue.action,
            'date': issue.date
        } for issue in issues]

    @join_point
    @authenticate
    def on_get_user_books(self, request, response):
        request.params['user_id'] = request.context.client.user_id
        books = self.issues.get_user_books(**request.params)
        response.media = books

    @join_point
    @authenticate
    def on_get_show_user(self, request, response):
        issue_u = self.issues.get_user_action()
        response.media = [{
            'issue_id': issue.id,
            'user_id': issue.id_user,
            'action': issue.action,
            'date': issue.date
        } for issue in issue_u]

    @join_point
    @authenticate
    def on_get_show_book(self, request, response):
        issue_b = self.issues.get_book_action()
        response.media = [{
            'issue_id': issue.id,
            'book_id': issue.id_book,
            'action': issue.action,
            'date': issue.date
        } for issue in issue_b]
