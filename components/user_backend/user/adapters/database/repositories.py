from typing import List, Optional

from user.application import interfaces
from user.application.dataclasses import User
from .tables import USER
from classic.components import component
from classic.sql_storage import BaseRepository
from sqlalchemy import delete, select, insert, func, desc


@component
class UsersRepo(BaseRepository, interfaces.UsersRepo):
    def get_by_id(self, user_id: int) -> Optional[User]:
        print(user_id)
        query = select(USER).where(USER.c.id == user_id)

        result = self.session.execute(query).fetchone()
        return result

    def add_instance(self, user: User):
        query = USER.insert().values(user_name=user.user_name)
        self.session.execute(query)
        new_user = select(USER).order_by(desc(USER.c.id))
        new_user = self.session.execute(new_user).fetchone()
        return {'id_user': new_user.id, 'name': new_user.name}

    def get_all(self) -> List[User]:
        query = select(USER)
        return self.session.execute(query).fetchall()

    def delete_instance(self, user_id: int):
        query = USER.delete().where(USER.c.id == user_id)
        return self.session.execute(query)
