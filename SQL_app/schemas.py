from optparse import Option
from typing import List, Optional

from pydantic import BaseModel

#from SQL_app.models import NewsArticles, StockHolders, Note


class NoteBase(BaseModel):
    NoteId: int
    Note: str
    OrgNumber: int


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    class Config:
        orm_mode = True



class NewsArticleBase(BaseModel):
    ArticlId: int
    URL: str
    Title: str
    OrgNumber: int


class NewsArticleCreate(NewsArticleBase):
    pass


class NewsArticle(NewsArticleBase):
    class Config:
        orm_mode = True

class AidBase(BaseModel):
    AidId: int
    Sum: int
    OrgNumber: int

class AidCreate(AidBase):
    pass

class Aid(AidCreate):
    class Config:
        orm_mode = True


class StockHolderBase(BaseModel):
    StockHolderId: int
    Name: str
    OrgNumber: int


class StockHolderCreate(StockHolderBase):
    pass


class StockHolder(StockHolderBase):
    class Config:
        orm_mode = True

class CompanyBase(BaseModel):
    OrgNumber: int
    CompanyName: Optional[str]
    Email: Optional[str]
    Sector: Optional[str]
    Description: Optional[str]
    Employees: Optional[int]
    Municipality: Optional[str]
    


class CompanyCreate(CompanyBase):
    pass


class Company(CompanyBase):
    Note: Optional[List[Note]]
    NewsArticle: Optional[List[NewsArticle]]
    Owner: Optional[List[StockHolder]]

    class Config:
        orm_mode = True

