import csv
import keyboard

class Reservation:

    def SingleRoom_Load(self):
        with open("Assets/SingleRoom.csv", mode='r', newline='', encoding="latin-1") as file:
            reader = csv.reader(file)
            # Skip the header row
            next(reader)
            SingleRooms = list(reader)  # Beolvassuk az összes sort egy listába
        return SingleRooms

    def DoubleRoam_Load(self):
        with open("Assets/DoubleRoom.csv", mode='r', newline='', encoding="utf-8") as file:
            reader = csv.reader(file)
            # Skip the header row
            next(reader)
            DoubleRooms = list(reader)  # Beolvassuk az összes sort egy listába
        return DoubleRooms

    def reservationForm(self):
        personCount = int(input("\nKérlek, add meg, hogy hány fővel utazol: "))
        if personCount == 1:
            SingleRooms = self.SingleRoom_Load()
            print("\nA számodra javasolt szobák: ")
            print("----------------------------------")
            for i, row in enumerate(SingleRooms):
                # A "Típus" mező az első oszlop (index 0)
                room_type = row[0]
                print(f"{i+1}. {room_type}")

            # Wait for a key press and get the key code
            key_code = keyboard.read_key()

            # Convert the key code to an integer and subtract 1 to get the index of the selected room
            selected_room = int(key_code) - 1

            if 0 <= selected_room < len(SingleRooms):
                print(f"\nKiválasztott szoba típusa: {SingleRooms[selected_room][0]}")
            else:
                print("\nNem választottál érvényes szobát.")
        if personCount == 2:
            DoubleRooms = self.DoubleRoam_Load()
            print("\nA számodra javasolt szobák: ")
            for i, row in enumerate(DoubleRooms):
                # A "Típus" mező az első oszlop (index 0)
                room_type = row[0]
                print(f"{i+1}. {room_type}")

            # Wait for a key press and get the key code
            key_code = keyboard.read_key()

            # Convert the key code to an integer and subtract 1 to get the index of the selected room
            selected_room = int(key_code) - 1

            if 0 <= selected_room < len(DoubleRooms):
                print(f"\nKiválasztott szoba típusa: {DoubleRooms[selected_room][0]}")
            else:
                print("\nNem választottál érvényes szobát.")

reservation = Reservation()
reservation.reservationForm()
