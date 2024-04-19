import json

class Hotel:
    def DataQuery(self):
        file_path = "BookingData.json"
        ID_get = input("Kérlek, add meg a foglalás azonosítóját: ")
        with open(file_path, mode='r', encoding="utf-8") as file:
            rooms_data = json.load(file)

        for room_data in rooms_data:
            if room_data["ID"] == ID_get:
                print(" ")
                print(f"Foglalás azonosítója: {room_data['ID']}")
                print(f"Szoba típusa: {room_data['Room']}")
                print(f"Szobaszám: {room_data['Room Number']}")
                print(f"Végösszeg: {room_data['Price']} Ft")
                print(f"Név: {room_data['Name']}")
                print(f"Születési dátum: {room_data['Birthdate']}")
                print(f"Bejelentkezés dátuma: {room_data['Checkin Date']}, {room_data['Checkin']}")
                print(f"Kijelentkezés dátuma: {room_data['Check-Out date']}, {room_data['Checkout']}")
Hotel = Hotel()
Hotel.DataQuery()