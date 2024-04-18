
import random  # ID generáláshoz szükséges
import string  # ID generáláshoz szükséges
import json

# from RoomDetails import SingleRoom, DoubleRoom

class Reservation:

    @staticmethod
    def id_generate(size):
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for x in range(size))

    def load_rooms(self, file_path):
        with open(file_path, mode='r', encoding="utf-8") as file:
            rooms_data = json.load(file)

        return rooms_data

    def reservationComplete(self, id, room, check_in_date, check_out_date, name, checkin, checkout, birthdate, file_path):
        reservation_data = {
            "ID": id,
            "Room": room,
            "Name": name,
            "Birthdate": birthdate,
            "Checkin Date": check_in_date,
            "Check-Out date": check_out_date,
            "Checkin": checkin,
            "Checkout": checkout,
        }
        try:
            with open("BookingData.json", mode="r", encoding="utf-8") as f:
                reservations = json.load(f)
        except FileNotFoundError:
            reservations = []
        reservations.append(reservation_data)
        with open("BookingData.json", mode="w", encoding="utf-8") as f:
            json.dump(reservations, f, ensure_ascii=False, indent=4)
        print("Sikeres foglalás!")
        print(reservation_data)
        # Kiválasztott szoba elérhető értékének csökkentése
        with open(file_path, mode='r', encoding="utf-8") as file:
            rooms_data = json.load(file)

        for room_data in rooms_data:
            if room_data["Típus"] == room:
                room_data["Elérhető"] -= 1
        # Frissített szobainformációk mentése
        with open(file_path, mode='w', encoding="utf-8") as file:
            json.dump(rooms_data, file, ensure_ascii=False, indent=4)

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
        check_in_date = input("Kérlek, add meg az utazásod dátumát (ÉÉÉÉ-HH-NN): ")
        check_out_date = input("Kérlek, add meg a kijelentkezésed dátumát (ÉÉÉÉ-HH-NN): ")
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

            self.reservationComplete(id, room,check_in_date,check_out_date, name, checkin, checkout, birthdate, file_path)
        else:
            print("\nNem választottál érvényes szobát.")


reservation = Reservation() # Inicializáljuk a Reservation class-t
reservation.reservation_form() # Meghívjuk a Reservation class ResetvationForm-ját