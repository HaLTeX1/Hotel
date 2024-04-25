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

    @staticmethod
    def DelReservation(id):
        file_name = "BookingData.json"
        # Fájl megnyitása olvasásra
        with open(file_name, 'r') as file:
            data = json.load(file)
        # Adott ID-vel rendelkező bejegyzés keresése és törlése
        for entry in data:
            if entry["ID"] == id:
                data.remove(entry)
                print(f"A(z) {id} azonosítójú bejegyzés sikeresen törölve.")
                break
        else:
            print(f"Nincs találat a(z) {id} azonosítójú bejegyzésre.")
        # Fájl újraírása frissített adatokkal
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)

    def listReservation(self):
        file_name = "BookingData.json"
        with open(file_name, mode="r", encoding="utf-8") as file:
            data = json.load(file)
        print(data)




