#OOP

#OBJECTS - things, items, they can do things, they have properties / attributes that describe

# emphasizes grouping data and functionality together in entities known as Objects

cat1 = {
    'name': 'Scar',
    'color': 'dark brown',
    'age': 3,
    'breed': 'lion'
}

cat2 = {
    'name': 'Garfield',
    'color': 'orange/striped',
    'age': 30,
    'breed': 'lasagna'
}

class Cat():
    def __init__(self, name, color, age, breed):
        self.name = name
        self.color = color
        self.age = age
        self.breed = breed
    
    def print_info(self):
        print(f"Name: {self.name} Color {self.color} Age {self.age} Breed {self.breed}")
        return self
    
    def meow(self):
        print(f"{self.name} lets out a cry: MEOOWWW")
        return self

cat1 = Cat("Scar", "dark brown", 3, 'lion')

print(cat1.name)
print(cat1.color)

cat1.print_info().meow().meow().print_info()