# StaySync - Szállásfoglaló rendszer

A program egy terminal alapú szállásfoglaló rendszert valósít meg. A program a Gábor Dénes Egyetem Objektumorientált Programozás *(MEIN-AN07)* kurzusára készült.

## A szoftver funkciói

A program lehetővé teszi egy fiktív hotelbe való szállásfoglalást, illetve a foglalások kezelését. 
- Foglalás 
- Foglalás törlése
- Foglalások listázása
- Adatlekérdezés (Foglalás ID alapján)

## Futási környezet
A program fő indító fájlja a **Hotel.py**. Ez hívja meg az összes további funkciót, és opciót. A program elindításához is ezt  fájlt szükséges elindítani az interpreter-ben.
```
Hotel.py
# Opciók listázása
print("1. Foglalás")
print("2. Lemondás")
print("3. Foglalási adatok lekérdezése")
print("4. Foglalások listázása")
print("\n")
sorszam = str(input("Kérlek, add meg a választott opció SORSZÁMÁT: "))


if sorszam == '1':
    reservation = Reservation() # Inicializáljuk a Reservation class-t
    reservation.reservation_form() # Meghívjuk a Reservation class ReservationForm-ját
elif sorszam == '2':
    Hotel = Hotel() # Inicializáljuk a Hotel class-t
    booking_id = input("Kérem adja meg az ID-t: ")
    Hotel.DelReservation(booking_id) # Booking ID alapján megkeressük az adathalmazt, és töröljük azt a JSON-ből
elif sorszam == '3':
    Hotel = Hotel() # Inicializáljuk a Hotel class-t
    Hotel.DataQuery() # Meghívjuk a Foglalás lekérdezésére szolgáló mechanizmust
elif sorszam == '4':
    Hotel = Hotel()  # Inicializáljuk a Hotel class-t
    Hotel.listReservation()
else:
    print("\nÉrvénytelen válasz")
```
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

### Szobaszám, árgenerálás
A szobaszámok, illetve az árak generálását a **RoomDetails.py** fájl teszi lehetővé
A szoba árait minden esetben random generálja a szoftver két megadott érték között:
 - SingleRoom esetén : **25.000 Ft - 35.000 Ft**
 - DoubleRoom esetén: **31.200 Ft - 42.500 Ft**

 A szobaszámok generálása hasonló módon megoldott SingleRoom és DoubleRoom esetén más-más értékek között generálja le a szobaszámot a szoftver
 - SingleRoom esetén:  **1 - 100 között**
 - DoubleRoom esetén: **101 - 200 között**
   
### Foglalás törlése

Foglalás törlését a foglaláskor, automatikusan generált ID segítségével kezdeményezhetjük. Amennyiben a megadott ID szerepel a **BookingData.json** fájlban abban az esetben a foglalás törlése megtörténik, egyéb esetben a tranzakció meghiúsul. 

### Foglalás lekérdezése

Egyéni foglalás lekérdezésére a **BookingData.json** fájlban tárolt ID segítségével van lehetőségünk. Az ID megadásával a szoftver kilistázza az összes vonatkozó foglalási adatot ami a megadott ID-hoz tartozik. 

### Összesített foglalási kimutatás

Van lehetőségünk lekérdezni egy összesített kimutatást, ami az összes **BookingData.json** fájlban megtalálható foglalást kilistázza összesítve, JSON formátumban. 

## JSON integráció

Foglalás kezdeményezésekor a személyek száma (*PersonCount*) alapján jeleníti meg részünkre a szoftver az elérhető szobákat. A szobák adatait az *Assets/SingleRoom.json, Assets/DoubleRoom.json* fájlokban tároljuk. 

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

## Felhasznált állományok, modulok
[JSON](https://docs.python.org/3/library/json.html)\
[Random](https://docs.python.org/3/library/json.html)\
[String](https://docs.python.org/3/library/string.html)
