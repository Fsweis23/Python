#Functions WHY?
#RETURN SOMETHING
#CAN BE CALLED
#SAVE SPACE
#REPEATABLE CODE

from sys import base_prefix

def function_name(parameter_one, parameter_two):
    pass

a = 59
b = 65
c = a+b
print(c)

a = 90
b = 80
c = a+b
print(c)

def determine_speed( hours, miles):
    print(f"Calculating speed when we travel {miles} miles in {hours} hours")
    # print(miles/hours)
    return miles/hours

print(determine_speed(3,150))

# def order_tacos(money, meat):

# def range(start, step = 1, stop = 0):