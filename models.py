from enum import Enum
from pydantic import BaseModel
from typing import Optional, List


class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    manager = "manager"

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]
