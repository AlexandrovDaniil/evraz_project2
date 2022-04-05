from typing import Optional

import attr


@attr.dataclass
class ActionUser:
    id_user: int
    action: str
    id: Optional[int] = None


@attr.dataclass
class Action:
    action: str
    obj_type: str
    id_book: Optional[int] = None
    id_user: Optional[int] = None
    id: Optional[int] = None
