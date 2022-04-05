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
        print(issues)
        response.media = [{
            'issue_id': issue[0],
            'book_id': issue[1],
            'user_id': issue[2],
            'action': issue[3],
            'date': issue[5]
        } for issue in issues]
