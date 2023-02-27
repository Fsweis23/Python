class Animal:
    def __init__(self):
        is_extinct = False

    def eat(self):
        print("the animal is eating!")

    def sleep(self):
        print("The animal is sleeping!")
    
    def mating(self):
        print("The animal is mating!")

class Lion(Animal):
    # pass
    def noise(self):
        print("rawr".upper())

class Rabbit(Animal):
    # pass
    def eat(self):
        print("The rabbit is eating a carrot...")

class Bear(Animal):
    # pass
    def sleep(self):
        random_number = random.randint(1, 10)
        if random_number == 7:
            print("The bear is hibernating!")
        else:
            print("It isn't winter yet!")

simba = Lion()
bugs_bunny = Rabbit()
yogi_bear = Bear()

# simba.eat()
# bugs_bunny.sleep()
# yogi_bear.mating()

simba.noise()
bugs_bunny.eat()
yogi_bear.sleep()

print("========================================================")

import random

class Animal:
    def __init__(self, name, species, region, is_extinct=False):
        super().__init__(name, species, region, is_extinct)
        self.name = name
        self.sleep = species
        self.region = region
        self.is_extinct = is_extinct

class Lion(Animal):
    def __init__(self, name, species, region, is_extinct=False):
        super().__init__(name, species, region, is_extinct)
        self.name = name
        self.sleep = species
        self.region = region
        self.is_extinct = is_extinct
    
    def noise(self):
        print("rawr".upper())

class Rabbit(Animal):
    def __init__(self, name, species, region, is_extinct=False):
        super().__init__(name, species, region, is_extinct)
        self.name = name
        self.sleep = species
        self.region = region
        self.is_extinct = is_extinct

    def eat(self):
        print("The rabbit is eating a carrot...")

class Dinosaur(Animal):
    def __init__(self, name, species, region, is_extinct=False):
        super().__init__(name, species, region, is_extinct)
        self.name = name
        self.sleep = species
        self.region = region
        self.is_extinct = is_extinct
        self.lefs = 4

simba = Lion("Simba", "Cat", "Africa")
mufasa = Lion("Mufasa", "Cat", "Africa")
bugs_bunny = Rabbit("Bugs Bunny", "Rabbit", "America")
little_foot = Dinosaur("Little Foot", "Dinosaur", "North America")


little_foot.is_extinct = True
print(little_foot.is_extinct)

print(simba.name, mufasa.name)

print(little_foot.legs)