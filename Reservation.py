import csv
import random  # ID generáláshoz szükséges
import string  # ID generáláshoz szükséges

# import RoomDetails

class Reservation:

    @staticmethod
    def id_generate(size):
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for x in range(size))

    def load_rooms(self, file_path):
        with open(file_path, mode='r', newline='', encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # fejléc átugrása
            rooms = list(reader)
        return rooms

    def reservationComplete(self, id, room, name, checkin, checkout, birthdate):
        self.id = id
        self.room = room
        self.name = name
        self.birthdate = birthdate
        self.checkin = checkin
        self.checkout = checkout
        with open("BookingData.csv", mode="a", encoding="latin-1", newline="") as BookingData:
            writer = csv.writer(BookingData)
            writer.writerow([self.id, self.room, self.name, self.birthdate, self.checkin, self.checkout])
        print("Sikeres foglalás!")
        print(self.id, self.room, self.name, self.birthdate, self.checkin, self.checkout)
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
                room = {rooms[selected_room - 1][0]}
                name = input("Kérlek, add meg a teljes neved: ")
                birthdate = input("Kérlek, add meg a születési dátumod (ÉÉÉÉ-HH-NN): ")
                checkin = input("Kérlek, add meg mikor szeretnél bejelentkezni (Óra : Perc): ")
                checkout = input("Kérlek, add meg mikor szeretnél kijelentkezni (Óra : Perc): ")
                id = self.id_generate(8)
                Reservation.reservationComplete(self,id, room, name, checkin, checkout, birthdate)
            else:
                print("\nNem választottál érvényes szobát.")
        except ValueError:
            print("\nHibás bemenet. Kérem, adjon meg egy számot.")
