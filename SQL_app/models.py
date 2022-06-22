from operator import index
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .database import Base

Base = declarative_base()

class Company(Base):
    __tablename__ = "Company"

    OrgNumber = Column(Integer, primary_key = True, index = True)
    CompanyName = Column(String)
    Email = Column(String)
    Sector = Column(String)
    Description= Column(String)
    Employees = Column(Integer)
    Municipality = Column(String)

    Notes = relationship("Note", back_populates="NoteAbout")
    NewsArticles = relationship("NewsArticle", back_populates="ArticleAbout")
    Owners = relationship("StockHolder", back_populates="HolderIn")
    Aid = relationship("Aid", back_populates = "AidTo")

class Note(Base):
    __tablename__ = "Note"

    NoteId = Column(Integer, primary_key = True, index=True)
    Note = Column(String)
    OrgNumber = Column(Integer, ForeignKey(Company.OrgNumber))

    NoteAbout = relationship("Company", back_populates="Note")

class NewsArticle(Base):
    __tablename__ = "NewsArticle"

    ArticleId = Column(Integer, primary_key=True, index = True)
    URL = Column(String)
    Title = Column(String)
    OrgNumber = Column(Integer, ForeignKey(Company.OrgNumber))
    
    ArticleAbout = relationship("Company", back_populates="NewsArticle")

class StockHolder(Base):
    __tablename__ = "StockHolder"
    
    StockHolderId = Column(Integer, primary_key = True, index=True)
    Name = Column(String)
    OrgNumber = Column(Integer, ForeignKey(Company.OrgNumber))
   
    HolderIn = relationship("Company", back_populates="Owner")

class Aid(Base):
    __tablename__ = "Aid"
    AidId = Column(Integer, primary_key = True, index=True)
    Sum = Column(Integer)
    OrgNumber = Column(Integer, ForeignKey(Company.OrgNumber))
    AidTo = relationship("Company", back_populates="Aid")
