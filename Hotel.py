from Reservation import Reservation
from DataQuery import Hotel

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