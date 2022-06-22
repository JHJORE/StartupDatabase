from sqlalchemy.orm import Session

from . import models, schemas


def get_Company(db: Session, OrgNumber_id: int):
    return db.query(models.Company).filter(models.Company.OrgNumber == OrgNumber_id).first()

def get_CompanyByName(db: Session, CompanyName: str):
    return db.query(models.Company).filter(models.Company.CompanyName == CompanyName).first()

def get_Companies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Company).offset(skip).limit(limit).all()

def get_Notes(db: Session, NoteId: int):
    return db.query(models.Notes).filter(models.Notes.NoteId == NoteId).first()

def get_NewsArticle(db: Session, NewsArticleId: int):
    return db.query(models.NewsArticle).filter(models.NewsArticle.ArticleId == NewsArticleId).first()

# def get_StockHolder(db: Session, skip: int = 0):
#     return db.query(models.StockHolders).offset(skip).all()




def delete_Company(db: Session, OrgNumber: int):
    db_Company = db.query(models.Company).filter(models.Company.OrgNumber == OrgNumber).first()
    db.delete(db_Company)
    db.commit()
    return db_Company

def delete_Note(db: Session, NoteId: int):
    db_Note = db.query(models.Notes).filter(models.Notes.NoteId == NoteId).first()
    db.delete(db_Note)
    db.commit()
    return db_Note

def delete_NewsArticle(db: Session, ArticleId: int):
    db_NewsArticle = db.query(models.NewsArticle).filter(models.NewsArticle.ArticleId == ArticleId).first()
    db.delete(db_NewsArticle)
    db.commit()
    return db_NewsArticle





def create_Company(db: Session, Company: schemas.CompanyCreate):
    db_Company = models.Company(OrgNumber = Company.OrgNumber, CompanyName = Company.CompanyName, Email = Company.Email, Sector = Company.Sector )
    db.add(db_Company)
    db.commit()
    db.refresh(db_Company)
    return db_Company

def create_Notes(db: Session, Notes: schemas.NotesCreate, OrgNumber: int):
    db_Notes = models.Notes(NoteId = Notes.NoteId, Notes = Notes.Notes, OrgNumber = OrgNumber)
    db.add(db_Notes)
    db.commit()
    db.refresh(db_Notes)
    return db_Notes


def create_NewsArticle(db: Session, NewsArticle: schemas.NewsArticleCreate, OrgNumber: int):
    db_NewsArticle = models.NewsArticle (ArticleId = NewsArticle.ArticleId, URL = NewsArticle.URL, Title = NewsArticle.Title, OrgNumber = OrgNumber)
    db.add(db_NewsArticle)
    db.commit()
    db.refresh(db_NewsArticle)
    return db_NewsArticle

def create_Stockholders (db: Session, StockHolders: schemas.StockHoldersCreate, OrgNumber: int):
    db_Stockholders = models.StockHolders(**StockHolders.dict(), stock = OrgNumber)
    db.add(db_Stockholders)
    db.commit()
    db.refresh(db_Stockholders)
    return db_Stockholders



def update_Company(db: Session, Company: schemas.Company, OrgNumber: int):
    db_Company = db.query(models.Company).filter(models.Company.OrgNumber == OrgNumber).first()
    db_Company.OrgNumber = OrgNumber
    db_Company.CompanyName = Company.CompanyName
    db_Company.Email = Company.Email
    db_Company.Sector = Company.Sector
    db.commit()
    db.refresh(db_Company)
    return db_Company


def update_NewsArticle(db: Session, NewsArticle: schemas.NewsArticle, ArticleId: int):
    db_NewsArticle = db.query(models.NewsArticle).filter(models.NewsArticle.ArticleId == ArticleId).first()
    db_NewsArticle.ArticleId = NewsArticle.ArticleId 
    db_NewsArticle.URL = NewsArticle.URL 
    db_NewsArticle.Title = NewsArticle.Title
    db_NewsArticle.OrgNumber = NewsArticle.OrgNumber
    db.commit()
    db.refresh(db_NewsArticle)
    return db_NewsArticle

def update_Note(db: Session, Note: schemas.Notes, NoteId: int):
    db_Note = db.query(models.Notes).filter(models.Notes.NoteId == NoteId).first()
    db_Note.NoteId = Note.NoteId
    db_Note.Notes = Note.Notes
    db_Note.OrgNumber = Note.OrgNumber
    db.commit()
    db.refresh(db_Note)
    return db_Note
