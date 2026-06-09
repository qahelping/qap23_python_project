"""
UserResponseCollapse allobject
Схема ответа с данными пользователя

idinteger
usernamestring
emailstring
rolestring
avatar_urlExpand all(string | null)
created_atstringdate-time
"""
from typing import Literal

from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: Literal["admin", "user"]
    avatar_url: str | None
    created_at: str


class RegisterAdminRequest(BaseModel):
    username: str
    email: str
    password: str
