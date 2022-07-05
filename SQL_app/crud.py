from ast import Raise
from sqlalchemy.orm import Session

from . import models, schemas


def get_Company(db: Session, OrgNumber_id: int):
    return db.query(models.Company).filter(models.Company.OrgNumber == OrgNumber_id).first()

def get_CompanyByName(db: Session, CompanyName: str):
    return db.query(models.Company).filter(models.Company.CompanyName.like(f"%Folkeinvest%")).first()

def get_Companies(db: Session, Municipality: str, Sector: int, EmployeesMin: int, EmployeesMax: int, skip: int = 0, limit: int = 100):
    return db.query(models.Company).filter(models.Company.Sector.like(f"%{Sector}%"), models.Company.Employees >= EmployeesMin, models.Company.Employees <= EmployeesMax, models.Company.Municipality.like(f"%{Municipality}%")).offset(skip).limit(limit).all()

def get_Note(db: Session, NoteId: int):
    return db.query(models.Note).filter(models.Note.NoteId == NoteId).first()

def get_NewsArticle(db: Session, NewsArticleId: int):
    return db.query(models.NewsArticle).filter(models.NewsArticle.ArticleId == NewsArticleId).first()


# def get_StockHolder(db: Session, skip: int = 0):
#     return db.query(models.StockHolder).offset(skip).all()

def get_Aids(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Aid).offset(skip).limit(limit).all()

def get_Aid(db: Session, AidId: str):
    return db.query(models.Aid).filter(models.Aid.AidId == AidId).first()

def get_CapitalRaise(db: Session, RaiseId: int):
    return db.query(models.CapitalRaise).filter(models.CapitalRaise.RaiseId == RaiseId).first()

def get_NoteByOrgNumber(db: Session, OrgNumber: int, skip: int = 0, limit: int = 100):
    return db.query(models.Note).filter(models.Note.OrgNumber == OrgNumber).offset(skip).limit(limit).all()





def delete_Company(db: Session, OrgNumber: int):
    db_Company = db.query(models.Company).filter(models.Company.OrgNumber == OrgNumber).first()
    db.delete(db_Company)
    db.commit()
    return db_Company

def delete_Note(db: Session, NoteId: int):
    db_Note = db.query(models.Note).filter(models.Note.NoteId == NoteId).first()
    db.delete(db_Note)
    db.commit()
    return db_Note

def delete_NewsArticle(db: Session, ArticleId: int):
    db_NewsArticle = db.query(models.NewsArticle).filter(models.NewsArticle.ArticleId == ArticleId).first()
    db.delete(db_NewsArticle)
    db.commit()
    return db_NewsArticle

def delete_Aid(db: Session, AidId: str):
    db_Aid = db.query(models.Aid).filter(models.Aid.AidId == AidId).first()
    db.delete(db_Aid)
    db.commit()
    return db_Aid

def delete_CapitalRaise(db: Session, RaiseId: int):
    db_CapitalRaise = db.query(models.CapitalRaise).filter(models.CapitalRaise.RaiseId == RaiseId).first()
    db.delete(db_CapitalRaise)
    db.commit()
    return db_CapitalRaise





def create_Company(db: Session, Company: schemas.CompanyCreate):
    db_Company = models.Company(OrgNumber = Company.OrgNumber, CompanyName = Company.CompanyName, Email = Company.Email, Sector = Company.Sector, Description = Company.Description, Employees = Company.Employees, Municipality = Company.Municipality, HomePage = Company.HomePage )
    db.add(db_Company)
    db.commit()
    db.refresh(db_Company)
    return db_Company

def create_Note(db: Session, Note: schemas.NoteCreate, OrgNumber: int):
    db_Note = models.Note(NoteId = Note.NoteId, Name = Note.Name, Note = Note.Note, OrgNumber = OrgNumber)
    db.add(db_Note)
    db.commit()
    db.refresh(db_Note)
    return db_Note


def create_NewsArticle(db: Session, NewsArticle: schemas.NewsArticleCreate, OrgNumber: int):
    db_NewsArticle = models.NewsArticle (ArticleId = NewsArticle.ArticlId, URL = NewsArticle.URL, Title = NewsArticle.Title, OrgNumber = OrgNumber)
    db.add(db_NewsArticle)
    db.commit()
    db.refresh(db_NewsArticle)
    return db_NewsArticle

def create_Stockholder (db: Session, StockHolder: schemas.StockHolderCreate, OrgNumber: int):
    db_StockHolder = models.StockHolder(**StockHolder.dict(), stock = OrgNumber)
    db.add(db_StockHolder)
    db.commit()
    db.refresh(db_StockHolder)
    return db_StockHolder

def create_Aid (db: Session, Aid: schemas.AidCreate, OrgNumber: int):
    db_Aid = models.Aid(AidId = Aid.AidId, Sum = Aid.Sum, GivenBy = Aid.GivenBy, Type = Aid.Type, Reason = Aid.Reason, County = Aid.County, DateGiven = Aid.DateGiven, OrgNumber = OrgNumber)
    db.add(db_Aid)
    db.commit()
    db.refresh(db_Aid)
    return db_Aid

def create_CapitalRaise (db: Session, CapitalRaise: schemas.CapitalRaiseCreate, OrgNumber: int):
    db_CapitalRaise = models.CapitalRaise(RaiseId = CapitalRaise.RaiseId, Sum = CapitalRaise.Sum, Link = CapitalRaise.Link, Date = CapitalRaise.Date, OrgNumber = OrgNumber)
    db.add(db_CapitalRaise)
    db.commit()
    db.refresh(db_CapitalRaise)
    return db_CapitalRaise





def update_Company(db: Session, Company: schemas.Company, OrgNumber: int):
    db_Company = db.query(models.Company).filter(models.Company.OrgNumber == OrgNumber).first()
    db_Company.OrgNumber = OrgNumber
    db_Company.CompanyName = Company.CompanyName
    db_Company.Email = Company.Email
    db_Company.Sector = Company.Sector
    db_Company.Employees = Company.Employees
    db_Company.Description = Company.Description
    db_Company.Municipality = Company.Municipality
    db_Company.HomePage = Company.HomePage
    db.commit()
    db.refresh(db_Company)
    return db_Company


def update_NewsArticle(db: Session, NewsArticle: schemas.NewsArticle, ArticleId: int):
    db_NewsArticle = db.query(models.NewsArticle).filter(models.NewsArticle.ArticleId == ArticleId).first()
    db_NewsArticle.ArticleId = NewsArticle.ArticlId 
    db_NewsArticle.URL = NewsArticle.URL 
    db_NewsArticle.Title = NewsArticle.Title
    db_NewsArticle.OrgNumber = NewsArticle.OrgNumber
    db.commit()
    db.refresh(db_NewsArticle)
    return db_NewsArticle

def update_Note(db: Session, Note: schemas.Note, NoteId: int):
    db_Note = db.query(models.Note).filter(models.Note.NoteId == NoteId).first()
    db_Note.NoteId = Note.NoteId
    db_Note.Name = Note.Name
    db_Note.Note = Note.Note
    db_Note.OrgNumber = Note.OrgNumber
    db.commit()
    db.refresh(db_Note)
    return db_Note

def update_Aid(db: Session, Aid: schemas.Aid, AidId: str):
    db_Aid = db.query(models.Aid).filter(models.Aid.AidId == AidId).first()
    db_Aid.AidId = Aid.AidId
    db_Aid.Sum = Aid.Sum
    db_Aid.OrgNumber = Aid.OrgNumber
    db_Aid.GivenBy = Aid.GivenBy
    db_Aid.Type = Aid.Type
    db_Aid.Reason = Aid.Reason
    db_Aid.County = Aid.County
    db_Aid.DateGiven = Aid.DateGiven
    db.commit()
    db.refresh(db_Aid)
    return db_Aid

def update_CapitalRaise(db: Session, CapitalRaise: schemas.CapitalRaise, RaiseId: int):
    db_CapitalRaise = db.query(models.CapitalRaise).filter(models.CapitalRaise.RaiseId == RaiseId).first()
    db_CapitalRaise.RaiseId = CapitalRaise.RaiseId
    db_CapitalRaise.Sum = CapitalRaise.Sum
    db_CapitalRaise.Link = CapitalRaise.Link
    db_CapitalRaise.Date = CapitalRaise.Date
    db.commit()
    db.refresh(db_CapitalRaise)
    return db_CapitalRaise
