from abc import ABC, abstractmethod


# step 1: Define the product interface
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass

# step 2: Implement concrete products

class Espresso(Coffee):
    def prepare(self):
        return "Preparing a rich and strong Espresso."
    

class Latte(Coffee):
    def prepare(self):
        return "Preparing a smooth and creamy Latte"
    
class Cappuccino(Coffee):
    def prepare(self):
        return "Preparing a frothy cappuccino."

# Step 3 : Implement the Factory (CoffeMachine)

class CoffeeMachine:

    def make_coffee(self, coffee_type):
        if coffee_type=="Espresso":
            return Espresso.prepare()
        elif coffee_type=="Latte":
            return Latte.prepare()
        elif coffee_type=="Cappuccino":
            return Cappuccino.prepare()
        else:
            return "Unknown Coffee type!"

# use the factory to create products

if __name__=="__main__":
    
    machine=CoffeeMachine()

    coffee=machine.make_coffee("Espresso")
    print(coffee) 
        