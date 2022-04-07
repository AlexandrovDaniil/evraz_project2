from abc import ABC, abstractmethod
from typing import List, Optional
from .dataclasses import Action


class IssuesRepo(ABC):

    @abstractmethod
    def add_action(self, action: Action): ...

    @abstractmethod
    def add_action_user(self, action: Action): ...

    @abstractmethod
    def add_action_book(self, action: Action): ...

    @abstractmethod
    def get_all(self) -> List[Action]: ...

    @abstractmethod
    def get_all_by_user(self, user_id: int) -> List[Action]: ...

    @abstractmethod
    def get_user_action(self) -> List[Action]: ...

    @abstractmethod
    def get_book_action(self) -> List[Action]: ...
