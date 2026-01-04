print("hello")
print(4+5)

class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def print_car(self):
        print(self.name)
        print(self.price)
        
bmw = Car("BMW", 1200)
bmw.print_car()