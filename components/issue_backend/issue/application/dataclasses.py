from typing import Optional
import attr


@attr.dataclass
class Action:
    action: str
    obj_type: str
    date: Optional[str] = None
    id_book: Optional[int] = None
    book_title: Optional[int] = None
    id_user: Optional[int] = None
    id: Optional[int] = None

