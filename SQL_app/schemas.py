from optparse import Option
from typing import List, Optional

from pydantic import BaseModel

#from SQL_app.models import NewsArticles, StockHolders, Notes


class NotesBase(BaseModel):
    NoteId: int
    Notes: str
    OrgNumber: int


class NotesCreate(NotesBase):
    pass


class Notes(NotesBase):
    class Config:
        orm_mode = True



class NewsArticleBase(BaseModel):
    ArticleId: int
    URL: str
    Title: str
    OrgNumber: int


class NewsArticleCreate(NewsArticleBase):
    pass


class NewsArticle(NewsArticleBase):
    class Config:
        orm_mode = True



class StockHoldersBase(BaseModel):
    StockHolderId: int
    Name: str
    OrgNumber: int


class StockHoldersCreate(StockHoldersBase):
    pass


class StockHolders(StockHoldersBase):
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
    Notes: Optional[List[Notes]]
    NewsArticles: Optional[List[NewsArticle]]
    Owners: Optional[List[StockHolders]]

    class Config:
        orm_mode = True