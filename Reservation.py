import csv
import RoomDetails

class Reservation:

    def load_rooms(self, file_path):
        with open(file_path, mode='r', newline='', encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # fejléc átugrása
            rooms = list(reader)
        return rooms

    def reservationComplete(self, name, checkin, checkout):
        self.name = name
        self.checkin = checkin
        self.checkout = checkout
        pass

    def reservation_form(self):
        person_count = int(input("\nKérlek, add meg, hogy hány fővel utazol: "))
        file_path = "Assets/SingleRoom.csv" if person_count == 1 else "Assets/DoubleRoom.csv"
        rooms = self.load_rooms(file_path)

        print("\nA számodra javasolt szobák: ")
        print("----------------------------")
        for i, room in enumerate(rooms):
            room_type = room[0]  # A "Típus" mező az első oszlop
            print(f"{i + 1}. {room_type}")
        selected_room = input("\nKérem, válasszon szobát: ")
        try:
            selected_room = int(selected_room)
            if 0 < selected_room <= len(rooms):
                print(f"\nKiválasztott szoba típusa: {rooms[selected_room - 1][0]}")
                name = input("Kérlek, add meg a teljes neved: ")
            else:
                print("\nNem választottál érvényes szobát.")
        except ValueError:
            print("\nHibás bemenet. Kérem, adjon meg egy számot.")
