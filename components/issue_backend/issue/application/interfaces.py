from abc import ABC, abstractmethod
from typing import List, Optional
from issue.application.dataclasses import Action


class IssuesRepo(ABC):

    @abstractmethod
    def add_action(self, action: Action): ...

    @abstractmethod
    def get_all(self) -> List[Action]: ...
