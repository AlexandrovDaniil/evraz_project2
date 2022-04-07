import json

import jwt

from user.application import services
from classic.components import component
from classic.http_auth import authenticate, authenticator_needed

from .join_points import join_point


@authenticator_needed
@component
class Users:
    users: services.Users

    @join_point
    def on_get_show_info(self, request, response):
        user = self.users.get_info(**request.params)
        response.media = {
            'user_id': user.id,
            'user_name': user.user_name
        }

    @join_point
    def on_post_add_user(self, request, response):
        self.users.add_user(**request.media)
        response.media = {'status': 'user added'}

    @join_point
    def on_get_show_all(self, request, response):
        users = self.users.get_all()
        response.media = [{'id': user.id,
                          'name': user.user_name}
                          for user in users]

    @join_point
    def on_get_delete_user(self, request, response):
        self.users.delete_user(**request.params)
        response.media = {'status': 'user deleted'}