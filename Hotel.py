import keyboard
import csv
Hotelek = []
with open("Hotels.json", "r", encoding='utf-8') as File:
    data = json.load(File)
    Hotelek.append(data)

print(Hotelek)

# Opciók listázása
print("1. Foglalás")
print("2. Lemondás")
print("3. Foglalás lemondása")
print("4. Foglalási adatok lekérdezése")
print("4. Foglalások listázása")
print("\n")

input_value = keyboard.read_key()


if input_value == '1':
    print("\nFoglalás")
elif input_value == '2':
    print("\nLemondás")
elif input_value == '3':
    print("\nLekérdezés")
elif input_value == '4':
    print("\nListázás")
else:
    print("\nÉrvénytelen válasz")