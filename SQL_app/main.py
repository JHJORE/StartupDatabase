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
    





@app.post("/Company/{OrgNumber}/Note/", response_model=schemas.Note)
def create_Note(
    OrgNumber: int, Note: schemas.Note, db: Session = Depends(get_db)
):
    return crud.create_Note(db=db, Note=Note, OrgNumber=OrgNumber)

@app.get("/Note/{NoteId}", response_model=schemas.Note)
def read_Note(NoteId: int, db: Session = Depends(get_db)):
    note = crud.get_Note(db=db, NoteId=NoteId)
    return note

@app.delete("/Note/{NoteId}/delete", response_model=schemas.Note)
def delete_Note(NoteId:int, db: Session = Depends(get_db)):
    db_Note = crud.delete_Note(db=db, NoteId=NoteId)
    return db_Note

@app.put("/Note/{NoteId}/update", response_model = schemas.Note)
def update_Note(NoteId:int, Note: schemas.Note, db: Session = Depends(get_db)):
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



@app.post("/Company/{OrgNumber}/Aid", response_model=schemas.Aid)
def create_Aid(
     OrgNumber: int, Aid: schemas.Aid, db: Session = Depends(get_db)
):
    return crud.create_NewsArticle(db=db, Aid=Aid, OrgNumber=OrgNumber)

@app.get("/Aid/{AidId}", response_model=schemas.Aid)
def read_Aid(AidId  : int, db: Session = Depends(get_db)):
    Aid = crud.get_Aid(db, AidId=AidId)
    return Aid

@app.delete("/Aid/{AidId}/delete", response_model=schemas.Aid)
def delete_Aid(AidId:int, db: Session = Depends(get_db)):
    db_Aid = crud.delete_Aid(db=db, AidId=AidId)
    return db_Aid

@app.put("/Aid/{AidId}/update", response_model = schemas.Aid)
def update_Aid(AidId:int, Aid: schemas.Aid, db: Session = Depends(get_db)):
    db_Aid = crud.update_Aid(AidId = AidId, Aid = Aid, db = db)
    return db_Aid



