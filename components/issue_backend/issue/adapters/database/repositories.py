from sqlalchemy import select

from issue.application import interfaces
from .tables import ACTION
from classic.components import component
from classic.sql_storage import BaseRepository
from issue.application.dataclasses import Action


@component
class IssuesRepo(BaseRepository, interfaces.IssuesRepo):

    def add_action(self, action: Action):
        query = ACTION.insert().values(obj_type=action.obj_type, id_user=action.id_user, id_book=action.id_book,
                                       action=action.action)
        self.session.execute(query)

    def get_all(self):
        query = select(ACTION)
        return self.session.execute(query).fetchall()