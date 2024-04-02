from pydantic import BaseModel
from typing import List, Optional

# pydantic -> 데이터 유효성 검증
class ItemBase(BaseModel):
    title: str
    description: str

class Item(ItemBase):
    id: int
    owner_id: int
    
    class Config:
        orm_mode = True # orm 방식으로 데이터 필드 읽기가 가능

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    title: Optional[str] = None
    description: Optional[str] = None

class UserBase(BaseModel):
    email: str

class User(UserBase):
    id: int
    email: str

    items: List[Item] = []

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    hashed_password: str

class UserUpdate(UserBase):
    email: str | None = None
    # email:Optional[str] = None (from typing import Optional) <- 3.9 이하 구버전에서 사용하는 코드
    password: str | None = None