from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    password: str

class UpdateUser(BaseModel):
    name: Optional[str]
    email: Optional[str]