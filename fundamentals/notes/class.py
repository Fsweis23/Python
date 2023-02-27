#python is an oop Language
#class are blueprints for creating objects
#good practice to have class name singular and capitalized

class Animal:
    #constructor are the properties of the class
    def __init__(self, name, species, region):
        self.name = name
        self.species = species
        self.region = region

    #methods are just functions that live inside of a class
    def message(self):
        print("This one goes out to my homie Sean!")
        return self
    
    def add(self, num1, num2):
        print(f"{self.name} is doing arithmetic! {num1} and {num2} = {num1+num2}")
        return self


#here we are creating an object of the class Animal
lion = Animal("Lion", "Cat", "Africa")
penguin = Animal("Penguin", "Bird/Mammal?", "Antartica")

print(lion.region)
# penguin.add(1,3)
penguin.message().add(7,3)

# Lion.region()