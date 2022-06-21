from operator import index
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Company(Base):
    __tablename__ = "company"

    OrgNumber = Column(Integer, primary_key = True, index = True)
    CompanyName = Column(String)
    Email = Column(String)
    Sector = Column(String)

    Notes = relationship("Notes", back_populates="NoteAbout")
    NewsArticles = relationship("NewsArticles", back_populates="ArticleAbout")
    Owners = relationship("StockHolders", back_populates="HolderIn")

class Notes(Base):
    __tablename__ = "Notes"

    NoteId = Column(Integer, primary_key = True, index=True)
    Notes = Column(String)
    OrgNumber = Column(Integer, ForeignKey(Company.OrgNumber))

    NoteAbout = relationship("Company", back_populates="Notes")

class NewsArticles(Base):
    __tablename__ = "NewsArticles"

    ArticleId = Column(Integer, primary_key=True, index = True)
    URL = Column(String)
    Title = Column(String)
    OrgNumber = Column(Integer, ForeignKey(Company.OrgNumber))
    
    ArticleAbout = relationship("Company", back_populates="NewsArticles")

class StockHolders(Base):
    __tablename__ = "StockHolders"
    
    StockHolderId = Column(Integer, primary_key = True, index=True)
    Name = Column(String)
    OrgNumber = Column(Integer, ForeignKey(Company.OrgNumber))
   
    HolderIn = relationship("Company", back_populates="Owners")
    


