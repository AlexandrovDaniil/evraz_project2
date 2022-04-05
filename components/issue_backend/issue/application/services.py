from typing import Optional, List

import jwt
from attr import asdict
from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from pydantic import validate_arguments
from classic.messaging import Message, Publisher

from . import errors, interfaces
from .dataclasses import Action

join_points = PointCut()
join_point = join_points.join_point

#
# class UserInfo(DTO):
#     id_user: int
#     action: str
#     id: Optional[int]


class ActionInfo(DTO):
    obj_type: str
    action: str
    id: Optional[int]
    id_book: Optional[int]
    id_user: Optional[int]


@component
class Issues:
    issue_repo: interfaces.IssuesRepo
    publisher: Optional[Publisher] = None

    @join_point
    @validate_arguments
    def message_distributor(self, obj_type: str, action: str, data: dict):
        action = Action(
            obj_type=obj_type,
            id_user=data['id'],
            # id_book=data['id_book'],
            action=action)
        print(action)

        # new_act = action.create_obj(action)
        self.issue_repo.add_action(action)

    # @join_point
    # @validate_with_dto
    # def add_user_action(self, user_info: UserInfo):
    #     new_act = user_info.create_obj(ActionUser)
    #     self.issue_repo.add_user_action(new_act)
    #
    # @join_point
    # @validate_with_dto
    # def add_book_action(self, book_info: BookInfo):
    #     new_act = book_info.create_obj(ActionBook)
    #     self.issue_repo.add_book_action(new_act)

    @join_point
    def get_all(self) -> List[Action]:
        users = self.issue_repo.get_all()
        return users
