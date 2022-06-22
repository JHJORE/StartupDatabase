from sql_app import main
from sql_app import models
from sql_app.database import SessionLocal

db = SessionLocal()

# orgNumber = 3
# companyName = "Lagt til med python"

# Company = models.Company (
#     OrgNumber = orgNumber,
#     CompanyName = companyName
# )

# print(Company.OrgNumber)

#main.create_Company(Company=Company)
# add_note = models.Note(
#     NoteId = 2,
#     Note = "Lagt til med python",
#     OrgNumber = 2
# )

# main.create_Note(Note= add_note, OrgNumber=2, db = db)

# note = main.read_Note(NoteId = 2, db = db)
# print(note)
# print(note.NoteId)
# print(note.Note)
# print(note.OrgNumber)

company = main.read_Company(OrgNumber = 2, db=db)
print(company.CompanyName)