import json

class Reservation:
    def reservationForm(self):
        city = input("Kérlek, add meg hova utaznál (Település): ")
        found = False
        # Végigiterálok az adatokon
        for hotel in data:
            if hotel['location'] == city:
                print(hotel['name'])  # Hotel nevének kiiratása település egyezése esetén
                personCount = int(input("Kérlek, add meg hány fővel utazol: "))
                for room in hotel["capacity"]:
                    if room["room_type"] == "egyágyas" and room["available_rooms"] > 0:
                        return True
                    else:
                        print("Nincs szabad egyágyas szoba a kiválaszott szálláshelyen 1 fő részére!")
                found = True
        if not found:
            print('A megadott településen nem tartunk nyílván szálláshelyeket!')

# Load data from JSON file
with open("Hotels.json") as f:
    data = json.load(f)

# Create an instance of the Reservation class
reservation = Reservation()

# Call the reservationForm method on the instance
reservation.reservationForm()
