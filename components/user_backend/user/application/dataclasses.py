from typing import Optional

import attr


@attr.dataclass
class User:
    user_name: str
    id: Optional[int] = None
