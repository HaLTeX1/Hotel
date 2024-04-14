import json

class Reservation:
    def __init__(self, data):
        self.data = data

    def reservationForm(self):
        city = input("Kérlek, add meg hova utaznál (Település): ")
        person_count = int(input("Kérlek, add meg hány fővel utazol: "))
        found = False
        hotels_in_city = []  # Lista az összes szállodára a városban
        for hotel in self.data:
            if hotel['location'] == city:
                hotels_in_city.append(hotel['name'])  # Hozzáadja a szállodát a listához
                one_bedroom_available = False
                for room in hotel["capacity"]:
                    if room["room_type"] == "egyágyas" and room["available_rooms"] >= person_count:
                        one_bedroom_available = True
                        break
                if one_bedroom_available:
                    print("Van szabad egyágyas szoba a kiválasztott szálláshelyen!")
                    found = True
                    break
        if not found:
            if not hotels_in_city:
                print('A megadott településen nem tartunk nyílván szálláshelyeket!')
            else:
                print('Nincs szabad egyágyas szoba a kiválaszott szálláshelyen', person_count, 'fő részére!')
        if hotels_in_city:  # Ha van találat, akkor kiírjuk a szállodák listáját
            print("Az összes szálláshely a városban:", hotels_in_city)


# Load data from JSON file
with open("Hotels.json") as f:
    data = json.load(f)

# Create an instance of the Reservation class and pass the data
reservation = Reservation(data)

# Call the reservationForm method on the instance
reservation.reservationForm()
