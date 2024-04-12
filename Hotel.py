import keyboard
import json

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
if keyboard.read_key() == '1':
    print("\nFoglalás")

if keyboard.read_key() == '2':
    print("\nLemondás")

if keyboard.read_key() == '3':
    print("\nLekérdezés")

if keyboard.read_key() == '4':
    print("\nListázás")
