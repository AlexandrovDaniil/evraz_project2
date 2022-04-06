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
        if obj_type == 'user':
            action = Action(
                obj_type=obj_type,
                id_user=data['id_user'],
                action=action)
            print(action)
            print('IM HERE USER IM HERE USER IM HERE USER')
            self.issue_repo.add_action_user(action)

        if obj_type == 'book':
            action = Action(
                obj_type=obj_type,
                id_book=data['id_book'],
                action=action)
            print(action)
            print('IM HERE IM HERE IM HERE IM HERE IM HERE IM HERE')
            self.issue_repo.add_action_book(action)

        if obj_type == 'user_book':
            action = Action(
                obj_type=obj_type,
                id_book=data['id_book'],
                id_user=data['id_user'],
                action=action)
            print(action)
            print('IM HERE IM HERE IM HERE IM HERE IM HERE IM HERE')
            self.issue_repo.add_action(action)


    @join_point
    def get_all(self) -> List[Action]:
        action = self.issue_repo.get_all()
        return action

    @join_point
    def get_user_action(self) -> List[Action]:
        user_act = self.issue_repo.get_user_action()
        return user_act

    @join_point
    def get_book_action(self) -> List[Action]:
        book_act = self.issue_repo.get_book_action()
        return book_act
