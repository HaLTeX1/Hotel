import keyboard
from Reservation import Reservation

# Opciók listázása
print("1. Foglalás")
print("2. Lemondás")
print("3. Foglalás lemondása")
print("4. Foglalási adatok lekérdezése")
print("4. Foglalások listázása")
print("\n")

input_value = keyboard.read_key()


if input_value == '1':
    reservation = Reservation() # Inicializáljuk a Reservation class-t
    reservation.reservation_form() # Meghívjuk a Reservation class ResetvationForm-ját
elif input_value == '2':
    print("\nLemondás")
elif input_value == '3':
    print("\nLekérdezés")
elif input_value == '4':
    print("\nListázás")
else:
    print("\nÉrvénytelen válasz")