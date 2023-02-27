from classes.pirate import Pirate
from classes.ninja import Ninja

pirate = Pirate("name")
ninja = Ninja("name")

while(pirate.health > 0 and ninja.health > 0):
    response = input("Your pirate, will you attack or defend? /n 1) attack /n 2) heal /n")
    if (response) == '1':
        pirate.attack(ninja)
    elif (response) == '2':
        pirate.heal
        print("Pirate heals")
    elif (response) == 3:
        print.level_up()
        print("pirate levels up")
    else:
        while (response != '1' and response != '2'):
            print("Please pick a valid option")
            response = input("You're a ninja, will you attack or defend? /n 1) attack /n 2) heal /n")
    roll = random.randint(1,3)
    if response == 1:
        ninja.attack(pirate)
        print("Ninja attacks")
    elif (response) == 2:
        ninja.heal
        print("ninja heals")
    elif response == 3:
        ninja.level_up()
        print("ninja levels up")

        print("pirate:")
        pirate.print_info()
        print("Ninja")
        ninja.print_info()

        if ninja.health > 0:
            print("ninja has defeated pirate")
        if pirate.health <= 0:
            print("pirate has defeated ninja")
