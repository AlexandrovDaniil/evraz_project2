from datetime import datetime

from sqlalchemy import select

from issue.application import interfaces
from .tables import ACTION, ACTION_USER, ACTION_BOOK
from classic.components import component
from classic.sql_storage import BaseRepository
from issue.application.dataclasses import Action


@component
class IssuesRepo(BaseRepository, interfaces.IssuesRepo):

    def add_action(self, action: Action):
        query = ACTION.insert().values(obj_type=action.obj_type, id_user=action.id_user, id_book=action.id_book,
                                       action=action.action, book_title=action.book_title, date=str(datetime.utcnow()))
        self.session.execute(query)

    def add_action_book(self, action: Action):
        query = ACTION_BOOK.insert().values(id_book=action.id_book, action=action.action, date=str(datetime.utcnow()))
        self.session.execute(query)

    def add_action_user(self, action: Action):
        query = ACTION_USER.insert().values(id_user=action.id_user, action=action.action, date=str(datetime.utcnow()))
        self.session.execute(query)

    def get_all(self):
        query = select(ACTION)
        return self.session.execute(query).fetchall()

    def get_all_by_user(self, user_id: int):
        query = select(ACTION).where(ACTION.c.id_user == user_id)
        return self.session.execute(query).fetchall()

    def get_user_action(self):
        query = select(ACTION_USER)
        return self.session.execute(query).fetchall()

    def get_book_action(self):
        query = select(ACTION_BOOK)
        return self.session.execute(query).fetchall()
