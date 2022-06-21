from sqlalchemy.orm import Session

from . import models, schemas


def get_Company(db: Session, OrgNumber_id: int):
    return db.query(models.Company).filter(models.Company.OrgNumber == OrgNumber_id).first()

def get_Notes(db: Session, NoteId: int):
    return db.query(models.Notes).filter(models.Notes.NoteId == NoteId).first()

def get_Article(db: Session, ArticleId: int):
    return db.query(models.NewsArticles).filter(models.NewsArticles.ArticleId == ArticleId).first()

def get_StockHolder(db: Session, skip: int = 0):
    return db.query(models.StockHolders).offset(skip).all()

def create_Notes(b: Session, Notes: schemas.NotesCreate):
    db_Notes = models.Company(NoteId = Notes.NoteId, Notes = Notes.Notes, OrgNumber = models.Company.OrgNumber, NoteAbout = Notes.NoteAbout)
    db.add(db_Notes)
    db.commit()
    db.refresh(db_Notes)
    return db_Notes


def create_NewsArticle(b: Session, NewsArticle: schemas.NewsArticleCreate):
    db_NewsArticle = models.Company (ArticleID = NewsArticle.ArticleId, URL = NewsArticle.URL, Title  = NewsArticle.Title, OrgNumber = models.Company.OrgNumber, ArticleAbout = NewsArticle.ArticleAbout)
    db.add(db_NewsArticle)
    db.commit()
    db.refresh(db_NewsArticle)
    return db_NewsArticle

def create_Company(db: Session, Company: schemas.CompanyCreate):
    db_Company = models.Company(OrgNumber = Company.OrgNumber, CompanyName = Company.CompanyName, Email = Company.Email, Sector = Company.Sector )
    db.add(db_Company)
    db.commit()
    db.refresh(db_Company)
    return db_Company


def create_Stockholders (db: Session, StockHolders: schemas.StockHoldersCreate, OrgNumber: int):
    db_Stockholders = models.StockHolders(**StockHolders.dict(), stock = OrgNumber)
    db.add(db_Stockholders)
    db.commit()
    db.refresh(db_Stockholders)
    return db_Stockholders