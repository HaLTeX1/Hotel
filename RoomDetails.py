from abc import ABC, abstractmethod
import random

class Room(ABC):
    def __init__(self, price, roomNumber):
        self._price = price
        self._roomNumber = roomNumber

    @abstractmethod
    def print_info(self):
        pass

def generate_room_details():
    SingleRoom_Price = random.randrange(25000, 35000)
    DoubleRoom_Price = random.randrange(31200, 42500)
    SingleRoom_Number = random.randint(1, 100)
    DoubleRoom_Number = random.randint(101, 200)
    return {
        "SingleRoom_Price": SingleRoom_Price,
        "DoubleRoom_Price": DoubleRoom_Price,
        "SingleRoom_Number": SingleRoom_Number,
        "DoubleRoom_Number": DoubleRoom_Number
    }

class SingleRoom(Room):
    def __init__(self, price, roomNumber):
        super().__init__(price, roomNumber)

    def print_info(self):
        print(f"A szoba száma: {self._roomNumber}, az ár: {self._price}")

class DoubleRoom(Room):
    def __init__(self, price, roomNumber):
        super().__init__(price, roomNumber)

    def print_info(self):
        print(f"A szoba száma: {self._roomNumber}, az ár: {self._price}")

