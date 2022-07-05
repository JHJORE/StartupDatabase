from datetime import date
from optparse import Option
from typing import List, Optional

from pydantic import BaseModel

from sql_app.database import Base


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
    URL: str
    Title: str
    OrgNumber: int



class NewsArticleCreate(NewsArticleBase):
    pass


class NewsArticle(NewsArticleBase):
    ArticleId: int
    class Config:
        orm_mode = True

class AidBase(BaseModel):
    AidId: str
    Sum: int
    GivenBy: str
    Type: str
    Reason: str
    County: Optional[str]
    DateGiven: Optional[date]
    OrgNumber: int

class AidCreate(AidBase):
    pass

class Aid(AidBase):
    class Config:
        orm_mode = True

class CapitalRaiseBase(BaseModel):
    RaiseId: int
    Sum: int
    Link: str
    Date: date
    OrgNumber: int

class CapitalRaiseCreate(CapitalRaiseBase):
    pass

class CapitalRaise(CapitalRaiseBase):
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
    HomePage: Optional[str]
    


class CompanyCreate(CompanyBase):
    pass


class Company(CompanyBase):
    Notes: Optional[List[Note]]
    NewsArticles: Optional[List[NewsArticle]]
    Owners: Optional[List[StockHolder]]
    Aid: Optional[List[Aid]]
    CapitalRaises: Optional[List[CapitalRaise]]

    class Config:
        orm_mode = True

