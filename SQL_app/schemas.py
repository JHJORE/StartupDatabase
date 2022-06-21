from typing import List, Optional

from pydantic import BaseModel


class CompanyBase(BaseModel):
    OrgNumber: str
    CompanyName: Optional[str]
    Email: Optional[str]
    Sector: Optional[str]
    


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
