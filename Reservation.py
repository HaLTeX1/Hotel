
import random  # ID generáláshoz szükséges
import string  # ID generáláshoz szükséges
import json
from datetime import datetime
from RoomDetails import SingleRoom, DoubleRoom, generate_room_details

class Reservation:

    @staticmethod
    def id_generate(size):
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for x in range(size))

    def load_rooms(self, file_path):
        with open(file_path, mode='r', encoding="utf-8") as file:
            rooms_data = json.load(file)

        return rooms_data

    def reservationComplete(self, id, room_type, room_number, price, check_in_date, check_out_date, name, checkin, checkout, birthdate, person_count, date, file_path):
        reservation_data = {
            "ID": id,
            "Room": room_type,
            "Room Number": room_number,
            "Price": price,
            "Name": name,
            "Birthdate": birthdate,
            "Checkin Date": check_in_date,
            "Check-Out date": check_out_date,
            "Checkin": checkin,
            "Checkout": checkout,
            "Person Count": person_count,
            "Date": date
        }
        try:
            with open("BookingData.json", mode="r", encoding="utf-8") as f:
                reservations = json.load(f)
        except FileNotFoundError:
            reservations = []
        reservations.append(reservation_data)
        with open("BookingData.json", mode="w", encoding="utf-8") as f:
            json.dump(reservations, f, ensure_ascii=False, indent=4)
        # print(reservation_data)
        print("Kérjük, a foglalás azonosítóját jegyezze fel, késöbb ezzel lesz lehetősége ügyintézésre!")
        print(f"\nSikeres foglalás! A foglalás azonosítója: {reservation_data['ID']}")

        # Szoba elérhetőségének csökkentése
        with open(file_path, mode='r', encoding="utf-8") as file:
            rooms_data = json.load(file)

        for room_data in rooms_data:
            if room_data["Típus"] == room_type:
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
        selected_room = int(input("\nKérem, válasszon szobát: "))
        check_in_date = input("Kérlek, add meg az utazásod dátumát (ÉÉÉÉ-HH-NN): ")
        check_out_date = input("Kérlek, add meg a kijelentkezésed dátumát (ÉÉÉÉ-HH-NN): ")
        selected_room = int(selected_room)
        if 0 < selected_room <= len(rooms):
            selected_room_data = rooms[selected_room - 1]
            print(f"\nKiválasztott szoba típusa: {selected_room_data['Típus']}")

            # Az ár és a szobaszám generálása
            room_details = generate_room_details()
            room_number = room_details["SingleRoom_Number"] if person_count == 1 else room_details["DoubleRoom_Number"]
            price = room_details["SingleRoom_Price"] if person_count == 1 else room_details["DoubleRoom_Price"]

            name = input("Kérlek, add meg a teljes neved: ")
            birthdate = input("Kérlek, add meg a születési dátumod (ÉÉÉÉ-HH-NN): ")
            checkin = input("Kérlek, add meg mikor szeretnél bejelentkezni (Óra : Perc): ")
            checkout = input("Kérlek, add meg mikor szeretnél kijelentkezni (Óra : Perc): ")
            id = self.id_generate(8)
            date =  datetime.today().strftime('%Y-%m-%d')
            self.reservationComplete(id, selected_room_data['Típus'], room_number, price, check_in_date, check_out_date, name, checkin, checkout, birthdate,person_count, date, file_path)
        else:
            print("\nNem választottál érvényes szobát.")
