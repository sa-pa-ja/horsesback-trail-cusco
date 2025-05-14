class Vehicle():
    def move(self):
        print("moving...")

class Car(Vehicle): # Car inherits from vehicle
    def honk(self):
        print("Beep beep!")
        
Car().honk()
Car().move()


class BankAccount():
    def __init__(self, balance):
        self.__balance = balance # private variable
    def deposit(self,amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
    
account = BankAccount(100)
account.deposit(500)
print(account.get_balance())


from abc import *

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass # Only define the idea
    
class Dog(Animal):
    def make_sound(self):
        print("Woof!!")
        
class Cat(Animal):
    def make_sound(self):
        print("Meow!!")

pet = Dog()
pet.make_sound()





