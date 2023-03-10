# instance method -- accesses or alters the actual object

# class method -- accesses of alters on the class level

#static method -- somehow related to the class but doesn't access or alter the class OR an instance

#these dictionaries will be used to instatiate cat objects
cat1_data = {
    'name': 'Scar',
    'color': 'dark brown',
    'age': 3,
    'breed': 'lion'
}

cat2_data = {
    'name': 'Garfield',
    'color': 'orange/striped',
    'age': 30,
    'breed': 'lasagna'
}

# Cat Class Definition
class Cat():
    #class attributes
    all_cats = []
    is_cute = True
    #constructor
    def __init__(self, cat_data, fav_toy_color, fav_toy_type, fav_toy_action):
        self.name = cat_data['name']
        self.color = cat_data['color']
        self.age = cat_data['age']
        self.breed = cat_data['breed']
        self.fav_toy = Toy(fav_toy_color, fav_toy_type, fav_toy_action)
        Cat.all_cats.append(self)
    
#string representation function -- special function that defines what we see if we print this object

    # def__repr__(self):
    #     return f"Name: {self.name} color: {self.color} age: {self.age} breed: {self.breed}"

    #instance method to print object info
    def print_info(self):
        print(f"Name: {self.name} color: {self.color} age: {self.age} breed: {self.breed}")
        print(f"My favorite toy is a {self.fav_toy.color} {self.fav_toy.type}")
        return self
    
    #instance method to make the cat meow
    def meow(self):
        print(f"{self.name} lets out a cry: MEOOWWW")
        return self
    
    #Class method! Hs access to the class, not any one instance
    def play(self):
        print(f"{self.name} plays with their {self.fav_toy.color} {self.fav_toy.type} and it {self.fav_toy.action}")
        return self

    #Static method -- cannot access class or instance, related functionality to the class
    @classmethod
    def print_all_cats(cls):
        for cat in cls.all_cats:
            # print(cat)
            cat.print_info()
    
    @staticmethod
    def convert_to_cat_years(years):
        return years * 7

#Toy class definition
class Toy():
    def __init__(self, type, color, action):
        self.type = type
        self.color = color
        self.action = action

#instantiating toys
ball = Toy('ball', 'red', 'bounces on the floor')
yarn = Toy('yarn', 'blue', 'rolls away')

#instantiating cats with toys info as well
cat1 = Cat(cat1_data, 'ball', 'red', 'bounces on the floor')
cat2 = Cat(cat2_data, 'yarn', 'blue', 'rolls away')
# print(cat1)
# cat1.fav_toy = ball

# print(cat1.fav_toy.type)
cat1.play()
cat2.play()
# Cat.print_all_cats()
# print(cat1.name)
# print(cat1.color)

# age = 20
# cat_years = cat1.convert_to_cat_years(age)
# print(cat_years)
# cat1.print_info().meow()

# print(Cat.all_cats)

# cat1.meow()
# cat1.meow()
# cat1.meow()
# cat1.meow()
# cat1.meow()
# cat1.meow()
# for one_cat in Cat.all_cats:
#     one_cat.print_info()
# one_cat could be anything