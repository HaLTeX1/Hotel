# StaySync - Szállásfoglaló rendszer

A program egy terminal alapú szállásfoglaló rendszert valósít meg. A program a Gábor Dénes Egyetem Objektumorientált Programozás *(MEIN-LA07)* kurzusára készült.

## A szoftver funkciói

A program lehetővé teszi egy fiktív hotelbe való szállásfoglalást, illetve a foglalások kezelését. 
- Foglalás 
- Foglalás törlése
- Foglalások listázása
- Adatlekérdezés (Foglalás ID alapján)

## A szoftver működése
### Foglalás

Foglalás generálásakor a rendelkezésre állók szobák függvényében van lehetőségünk foglalás létrehozására. A foglalás létrehozásakor a foglalás adatait a **BookingData.json** fájlba menti a szoftver egy előre megadott szintaxis alapján.

```
BookingData.json
[
    {
        "ID": "8D7Z7WXB",
        "Room": "Összekötő Odú",
        "Room Number": 167,
        "Price": 35576,
        "Name": "Réz Levente László",
        "Birthdate": "2004-05-01",
        "Checkin Date": "2024-04-25",
        "Check-Out date": "2024-04-26",
        "Checkin": "10:00",
        "Checkout": "15:00",
        "Person Count": 2
    }
]
```

### Foglalás törlése

Foglalás törlését a foglaláskor, automatikusan generált ID segítségével kezdeményezhetjük. Amennyiben a megadott ID szerepel a **BookingData.json** fájlban abban az esetben a foglalás törlése megtörténik, egyéb esetben a tranzakció meghiúsul. 

### Foglalás lekérdezése

Egyéni foglalás lekérdezésére a **BookingData.json** fájlban tárolt ID segítségével van lehetőségünk. Az ID megadásával a szoftver kilistázza az összes vonatkozó foglalási adatot ami a megadott ID-hoz tartozik. 

### Összesített foglalási kimutatás

Van lehetőségünk lekérdezni egy összesített kimutatást, ami az összes **BookingData.json** fájlban megtalálható foglalást kilistázza összesítve, JSON formátumban. 

## JSON integráció

Foglalás kezdeményezésekor a személyek száma (*PersonCount*) alapján jeleníti meg részünkre a szoftver az elérhető szobákat. A szobák adatait az *Assets/SingleRoom.json, Assets/DoubleRoom.json* tároljuk. 

```
SingleRoom.json
[
    {
        "Típus": "Magányos Menedék",
        "Összesen": 3,
        "Elérhető": 1
    },
    {
        "Típus": "Egyedi Zuga",
        "Összesen": 3,
        "Elérhető": 2
    },
    {
        "Típus": "Kuckó Kuckó",
        "Összesen": 4,
        "Elérhető": 3
    },
[...]
]
```
