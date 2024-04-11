from abc import ABC, abstractmethod
import random

class Room(ABC):
    def __init__(self, price, roomNumber):
        self._price = price
        self._roomNumber = roomNumber

    @abstractmethod
    def print_info(self):
        pass

class SingleRoom(Room):
    def __init__(self, price, roomNumber):
        super().__init__(price, roomNumber)

    def print_info(self):
        print(f"A szoba száma: {self._roomNumber}, az ár: {self._price}")

SingleRoom_Price = random.randrange(25000, 35000)

# Példa használat:
room = SingleRoom(SingleRoom_Price, 65)
room.print_info()
