# from game_classes import character
from game_classes.character import Character
from game_classes.pokemon import Pokemon
import random

bob = Character()
bulbasaur = Pokemon('grass', 50)

while(bob.health > 0 and bulbasaur.health > 0):
    # \n will add a line break
    response = input("You're bob, will you attack or defend? \n 1) attack \n 2) defend")
    if response == '1':
        bob.attack(bulbasaur)
    elif response == '2':
        bob.heal()
    else:
        print("Please pick a valid option")
    
    roll = random.randint(1,3)
    if roll == 1:
        bulbasaur.attack(bob)
        print("bulbasaur attacks")
    elif roll == 2:
        bulbasaur.heal()
        print("bulbasaur defends")
    elif roll == 3:
        bulbasaur.level_up()
        print("bulbasaur levels up")
    
    print("Bob:")
    bob.print_info()
    print("Bulba")
    bulbasaur.print_info()

if bulbasaur.health > 0:
    print("Bulba haas defeated bob")
if bob.health > 0:
    print("Bob has defeated bulba")
if bob.health <= 0 and bulbasaur <= 0:
    print("They knocked each other out")