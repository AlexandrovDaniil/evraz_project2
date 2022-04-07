from typing import Optional, List, Dict

from classic.app import DTO
from classic.aspects import PointCut
from classic.components import component
from pydantic import validate_arguments

from . import errors, interfaces
from .dataclasses import Action

join_points = PointCut()
join_point = join_points.join_point


class ActionInfo(DTO):
    obj_type: str
    action: str
    id: Optional[int]
    id_book: Optional[int]
    book_title: Optional[int]
    id_user: Optional[int]


@component
class Issues:
    issue_repo: interfaces.IssuesRepo

    @join_point
    @validate_arguments
    def message_distributor(self, obj_type: str, action: str, data: dict):
        if obj_type == 'user':
            action = Action(
                obj_type=obj_type,
                id_user=data['id_user'],
                action=action)
            self.issue_repo.add_action_user(action)
        elif obj_type == 'book':
            action = Action(
                obj_type=obj_type,
                id_book=data['id_book'],
                action=action)
            self.issue_repo.add_action_book(action)
        elif obj_type == 'user_book':
            action = Action(
                obj_type=obj_type,
                id_book=data['id_book'],
                id_user=data['id_user'],
                book_title=data['book_title'],
                action=action)
            self.issue_repo.add_action(action)
        else:
            raise errors.WrongObjType(obj_type=obj_type)

    @join_point
    def get_all(self) -> List[Action]:
        action = self.issue_repo.get_all()
        return action

    @join_point
    def get_all_by_user(self, user_id: int) -> List[Action]:
        action = self.issue_repo.get_all_by_user(user_id)
        return action

    @join_point
    def get_user_books(self, user_id: int) -> Dict:
        actions = self.issue_repo.get_all_by_user(user_id)
        books_dict = {}
        for action in actions:
            if action.action == 'take':
                books_dict[action.id_book] = action.book_title
            if action.action == 'return':
                books_dict.pop(action.id_book)
        return books_dict

    @join_point
    def get_user_action(self) -> List[Action]:
        user_act = self.issue_repo.get_user_action()
        return user_act

    @join_point
    def get_book_action(self) -> List[Action]:
        book_act = self.issue_repo.get_book_action()
        return book_act
