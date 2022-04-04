from typing import Optional, List

import jwt
from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from pydantic import validate_arguments

from . import errors, interfaces
from .dataclasses import User

join_points = PointCut()
join_point = join_points.join_point


class UserInfo(DTO):
    user_name: str
    id: Optional[int]


@component
class Users:
    user_repo: interfaces.UsersRepo

    @join_point
    @validate_arguments
    def get_info(self, id: int):
        user = self.user_repo.get_by_id(id)
        if not user:
            raise errors.NoUser(id=id)
        return user

    @join_point
    @validate_with_dto
    def add_user(self, user_info: UserInfo):
        new_user = user_info.create_obj(User)
        self.user_repo.add_instance(new_user)

    @join_point
    @validate_arguments
    def delete_user(self, id: int):
        user = self.user_repo.get_by_id(id)
        if not user:
            raise errors.NoUser(id=id)
        self.user_repo.delete_instance(id)

    @join_point
    def get_all(self) -> List[User]:
        users = self.user_repo.get_all()
        return users
