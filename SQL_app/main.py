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


# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


@app.get("/Company/{OrgNumber}", response_model=schemas.Company)
def read_Company(OrgNumber: int, db: Session = Depends(get_db)):
    db_Company = crud.get_Company(db, OrgNumber_id=OrgNumber)
    if db_Company is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_Company


@app.post("/Company/{OrgNumber}/Notes/", response_model=schemas.Notes)
def create_Note(
    OrgNumber: int, Notes: schemas.Notes, db: Session = Depends(get_db)
):
    return crud.create_Notes(db=db, Notes=Notes, OrgNumber=OrgNumber)


# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items

@app.get("/Notes/{NoteId}", response_model=schemas.Notes)
def read_Note(NoteId: int, db: Session = Depends(get_db)):
    note = crud.get_Notes(db, NoteId=NoteId)
    return note
