from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
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
    HomePage = Column(String)

    Notes = relationship("Note", back_populates="NoteAbout")
    NewsArticles = relationship("NewsArticle", back_populates="ArticleAbout")
    Owners = relationship("StockHolder", back_populates="HolderIn")
    Aid = relationship("Aid", back_populates = "AidTo")
    CapitalRaises = relationship("CapitalRaise", back_populates="CapitalRaiseComp")

class Note(Base):
    __tablename__ = "Note"

    NoteId = Column(Integer, primary_key = True, index=True)
    Note = Column(String)
    OrgNumber = Column(Integer, ForeignKey(Company.OrgNumber))

    NoteAbout = relationship("Company", back_populates="Notes")

class NewsArticle(Base):
    __tablename__ = "NewsArticle"

    ArticleId = Column(Integer, primary_key=True, index = True)
    URL = Column(String)
    Title = Column(String)
    OrgNumber = Column(Integer, ForeignKey(Company.OrgNumber))
    
    ArticleAbout = relationship("Company", back_populates="NewsArticles")

class StockHolder(Base):
    __tablename__ = "StockHolder"
    
    StockHolderId = Column(Integer, primary_key = True, index=True)
    Name = Column(String)
    OrgNumber = Column(Integer, ForeignKey(Company.OrgNumber))
   
    HolderIn = relationship("Company", back_populates="Owners")

class Aid(Base):
    __tablename__ = "Aid"
    AidId = Column(String(100), primary_key = True, index=True)
    Sum = Column(Integer)
    GivenBy = Column(String)
    Type = Column(String)
    Reason = Column(String)
    County = Column(String)
    DateGiven = Column(Date)
    OrgNumber = Column(Integer, ForeignKey(Company.OrgNumber))
    AidTo = relationship("Company", back_populates="Aid")


class CapitalRaise(Base):
    __tablename__ = "CapitalRaise"
    RaiseId = Column(Integer, primary_key = True, index=True)
    Sum = Column(Integer)
    Link = Column(String)
    Date = Column(Date)

    OrgNumber = Column(Integer, ForeignKey(Company.OrgNumber))
    CapitalRaiseComp = relationship("Company", back_populates="CapitalRaises")
