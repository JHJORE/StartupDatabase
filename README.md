# StartupDatabase
Dette er en database og en script som henter data fra ulike kilder som Brønnøysundsregisteret, proff.no og StartupMatcher.

For å migrere databasen kjør:
alembic upgrade head

For å automatisk lage revision script som skal migreres kjør:

alembic revision --autogenerate -m "beskrivende filnavn"

For å åpne nettbassert api kjør:
uvicorn sql_app.main:app --reload
