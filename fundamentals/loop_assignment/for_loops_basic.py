# Basic - Print all integers from 0 to 150.

for i in range(0, 151):
        print(i)

print('======================================')

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000.

for x in range(5, 1001, 5):
        print(x)

print('======================================')

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for a in range(1, 101):
        if a % 10 == 0:
                print("Coding Dojo")
        elif a % 5 == 0:
                print(a, "coding")
        else:
                print(a)

print('======================================')

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

oddNum = 0
min = 0
max = 500000

for count in range(min, max + 1):
        if i % 2 == 0:
                print("{0}".format(count))
                oddNum = oddNum + count

print("final sum from {0} to {1} = {2}".format(min, max, oddNum))

print('======================================')

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

def countDown():
        year = 2018
        while year > 0:
                print(year)
                year = year - 4

countDown()

print('======================================')

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines).

def flexible_counter(lowNum, highNum, mult):
        for i in range(lowNum, highNum):
                if i % mult == 0:
                        print(i)

flexible_counter(2,9,3)

print('======================================')