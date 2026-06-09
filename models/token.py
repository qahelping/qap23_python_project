from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

"""
TokenResponseCollapse allobject
Схема ответа с токеном

access_tokenstring
token_typeCollapse allstring
Default"bearer"
"""

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = Field(default='bearer')




