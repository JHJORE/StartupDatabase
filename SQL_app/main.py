from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/Company/", response_model=schemas.Company)
def create_Company(Company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    #db_user = crud.get_user_by_email(db, email=user.email)
    #if db_user:
    #    raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_Company(db=db, Company=Company)


@app.get("/Company/", response_model=List[schemas.Company])
def read_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    companies = crud.get_Companies(db, skip=skip, limit=limit)
    return companies


@app.get("/Company/{OrgNumber}", response_model=schemas.Company)
def read_Company(OrgNumber: int, db: Session = Depends(get_db)):
    db_Company = crud.get_Company(db, OrgNumber_id=OrgNumber)
    if db_Company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_Company


@app.get("/Company/{CompanyName}", response_model=schemas.Company)
def read_Company_By_Name(CompanyName: str, db: Session = Depends(get_db)):
    db_Company = crud.get_CompanyByName(db, CompanyName=CompanyName)
    if db_Company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_Company

@app.delete("/Company/{OrgNumber}/delete", response_model=schemas.Company)
def delete_Company(OrgNumber:int, db: Session = Depends(get_db)):
    db_Company = crud.delete_Company(db, OrgNumber=OrgNumber)
    return db_Company

@app.put("/Company/{OrgNumber}/update", response_model= schemas.Company)
def update_Company(OrgNumber: int, Company: schemas.Company, db: Session = Depends(get_db)):
    db_Company = crud.update_Company(db = db, Company=Company, OrgNumber=OrgNumber)
    return db_Company
    





@app.post("/Company/{OrgNumber}/Notes/", response_model=schemas.Notes)
def create_Note(
    OrgNumber: int, Notes: schemas.Notes, db: Session = Depends(get_db)
):
    return crud.create_Notes(db=db, Notes=Notes, OrgNumber=OrgNumber)

@app.get("/Notes/{NoteId}", response_model=schemas.Notes)
def read_Note(NoteId: int, db: Session = Depends(get_db)):
    note = crud.get_Notes(db=db, NoteId=NoteId)
    return note

@app.delete("/Notes/{NoteId}/delete", response_model=schemas.Notes)
def delete_Note(NoteId:int, db: Session = Depends(get_db)):
    db_Note = crud.delete_Note(db=db, NoteId=NoteId)
    return db_Note

@app.put("/Notes/{NoteId}/update", response_model = schemas.Notes)
def update_Note(NoteId:int, Note: schemas.Notes, db: Session = Depends(get_db)):
    db_Note = crud.update_Note(NoteId = NoteId, Note = Note, db = db)
    return db_Note





@app.post("/Company/{OrgNumber}/NewsArticle", response_model=schemas.NewsArticle)
def create_NewsArticle(
     OrgNumber: int, NewsArticle: schemas.NewsArticle, db: Session = Depends(get_db)
):
    return crud.create_NewsArticle(db=db, NewsArticle=NewsArticle, OrgNumber=OrgNumber)

@app.get("/NewsArticle/{NewsArticleId}", response_model=schemas.NewsArticle)
def read_NewsArticle(NewsArticleId: int, db: Session = Depends(get_db)):
    newsArticle = crud.get_NewsArticle(db, NewsArticleId=NewsArticleId)
    return newsArticle

@app.delete("/NewsArticle/{ArticleId}/delete", response_model=schemas.NewsArticle)
def delete_NewsArticle(ArticleId:int, db: Session = Depends(get_db)):
    db_Note = crud.delete_NewsArticle(db=db, ArticleId=ArticleId)
    return db_Note

@app.put("/NewsArticle/{ArticleId}/update", response_model=schemas.NewsArticle)
def update_NewsArticle(ArticleId: int, NewsArticle: schemas.NewsArticle, db: Session = Depends(get_db)):
    db_NewsArticle = crud.update_NewsArticle(ArticleId=ArticleId, NewsArticle=NewsArticle, db=db)
    return db_NewsArticle