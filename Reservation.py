
import random  # ID generáláshoz szükséges
import string  # ID generáláshoz szükséges
import json

# import RoomDetails

class Reservation:

    @staticmethod
    def id_generate(size):
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for x in range(size))

    def load_rooms(self, file_path):
        with open(file_path, mode='r', encoding="utf-8") as file:
            rooms_data = json.load(file)
        return rooms_data

    def reservationComplete(self, id, room, name, checkin, checkout, birthdate):
        reservation_data = {
            "ID": id,
            "Room": room,
            "Name": name,
            "Birthdate": birthdate,
            "Checkin": checkin,
            "Checkout": checkout
        }
        with open("BookingData.json", mode="a", encoding="utf-8") as booking_file:
            json.dump(reservation_data, booking_file, ensure_ascii=False)
            booking_file.write("\n")
        print("Sikeres foglalás!")
        print(reservation_data)

    def reservation_form(self):
        person_count = int(input("\nKérlek, add meg, hogy hány fővel utazol: "))
        file_path = "Assets/SingleRoom.json" if person_count == 1 else "Assets/DoubleRoom.json"
        rooms = self.load_rooms(file_path)

        print("\nA számodra javasolt szobák: ")
        print("----------------------------")
        for i, room in enumerate(rooms, 1):
            room_type = room["Típus"]
            print(f"{i}. {room_type}")
        selected_room = input("\nKérem, válasszon szobát: ")
        try:
            selected_room = int(selected_room)
            if 0 < selected_room <= len(rooms):
                selected_room_data = rooms[selected_room - 1]
                print(f"\nKiválasztott szoba típusa: {selected_room_data['Típus']}")
                room = selected_room_data["Típus"]
                name = input("Kérlek, add meg a teljes neved: ")
                birthdate = input("Kérlek, add meg a születési dátumod (ÉÉÉÉ-HH-NN): ")
                checkin = input("Kérlek, add meg mikor szeretnél bejelentkezni (Óra : Perc): ")
                checkout = input("Kérlek, add meg mikor szeretnél kijelentkezni (Óra : Perc): ")
                id = self.id_generate(8)
                self.reservationComplete(id, room, name, checkin, checkout, birthdate)
            else:
                print("\nNem választottál érvényes szobát.")
        except ValueError:
            print("\nHibás bemenet. Kérem, adjon meg egy számot.")

reservation = Reservation() # Inicializáljuk a Reservation class-t
reservation.reservation_form() # Meghívjuk a Reservation class ResetvationForm-ját