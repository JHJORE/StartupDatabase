# StartupDatabase
Systeminfo

For å migrere databasen kjør:
alembic upgrade head

For å automatisk lage revision script som skal migreres kjør:

alembic revision --autogenerate -m "beskrivende filnavn"

For å åpne nettbasert api kjør:
uvicorn sql_app.main:app --reload



DOKUMENTASJON
Meningen med programmet er å hente inn data for å kunne finne selskaper i mikrocapsegmentet.
Programmet gjør dette ved å først lese gjennom en csv fil lastet ned fra Innovasjon Norge og data om tilsagn hentet fra Brønnøysundregisteret.
Bare selskaper nevnt i dataen over vil bli lagt til i databasen. Det første som skjer er at programmet leser dataen. Programmet vil fortløpende
legge til selskaper. Møter programmet på et selskap som allerede har mottatt støtte eller tilskudd vil bare tilskuddet bli lagt til (bedriften
ble lagt til første gang programmet leser at den har fått støtte). Et selskaps kapitalutvidelser vil ikke bli hentet før senere, grunnen 
vil blir forklart senere

Det grafiske grensesnittet består av flere sider. Det første som møter brukeren er en hjemmeside der alle selskapene som ligger i databasen 
fremstilles i en tabell med utvalgt informasjon om selskapet. På denne siden er det mulig å filtrer hvilke selskaper som vises basert på følgende:
selskapsnavn, sektor, kommune, minimum og maksimum antall ansatte. Herfra kan du også manuelt slette selskaper som ikke er relevante fra databasen.
I tabellen kan en bruker dobbelklikke på et selskap for å bli tatt videre til en side med mer informasjon om nevnt selskap. Her kan du manuelt
slette og endre informasjonen om bedriften. Du kan ikke endre organisasjonsnummer. Brukeren kan legge til og endre notater om bedriften. Brukeren
kan også legge til nyhetsartikler om bedriften. Første tabell fra toppen inneholder alle støtteordninger og tilsagn bedriften har fått. Etter
vår erfaring med å skumme gjennom dataen er det ikke stort overlapp mellom selskaper som har mottat tilsagn og selskaper som har mottat støtte
fra innovasjon Norge. Dette er ikke definitivt. Andre tabell fra toppen inneholder kapitalutvidelser. Kapitalutvidelsene blir hentet når en bruker
dobbeltrykker på bedriften i tabellen på hjemmesiden. Dette er fordi for å hente kapitalutvidelser fra nettet må en gjøre ett kall per bedrift.
Dette er svært ineffektivt og er unødvendig å gjøre for alle bedrifter i databasen. 

Merk: Dataen fra Innovasjon Norge inneholder noe støy for eksempel Landbrukstilskudd, og dataen fra Brønnøysundregisteret har noe annet støy for eksempel
en del skattelettelser som ikke nødvendigvis er relevant.

Videre utvikling:
 - Lage en liste over "favorittbedrifter" slik at de mest aktuelle bedriftene blir lagt til i en egen liste.
 - Koble opp Liste-ikonet med Notater i NavBar
 - Automatisk oppdatering av data
 - Samle inn data fra andre steder, eksempelvis StartupMatcher og Proff.no
 - Gjøre grafiske grensesnittet penere og mer brukervennlig
 - Legge til flere attributter en kan filtrere på
 - Dark Mode


