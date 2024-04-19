import keyboard
from Reservation import Reservation
from DataQuery import Hotel

# Opciók listázása
print("1. Foglalás")
print("2. Lemondás")
print("3. Foglalási adatok lekérdezése")
print("4. Foglalások listázása")
print("\n")

input_value = keyboard.read_key()


if input_value == '1':
    reservation = Reservation() # Inicializáljuk a Reservation class-t
    reservation.reservation_form() # Meghívjuk a Reservation class ReservationForm-ját
elif input_value == '2':
    Hotel = Hotel() # Inicializáljuk a Hotel class-t
    booking_id = input("Kérem adja meg az ID-t: ")
    Hotel.DelReservation(booking_id) # Booking ID alapján megkeressük az adathalmazt, és töröljük azt a JSON-ből
elif input_value == '3':
    Hotel = Hotel() # Inicializáljuk a Hotel class-t
    Hotel.DataQuery() # Meghívjuk a Foglalás lekérdezésére szolgáló mechanizmust
elif input_value == '4':
    print("\nListázás")
else:
    print("\nÉrvénytelen válasz")