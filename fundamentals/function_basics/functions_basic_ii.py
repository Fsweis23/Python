# ! Countdown - Create a function that accepts a number as an input. Retur a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countDown(number):
    arr = []
    for i in range(number, -1, -1):
        arr.append(i)
    
    arr.pop(5)
    return arr

print(countDown(5))
print('======================================')

# ! Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def print_and_return(a_list):
    print(a_list[0])
    return a_list[1]

print_and_return(['a', 'b'])
print('======================================')

# ! First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def firstPlusLength(a_list):
    return a_list[0] + len(a_list)

print(firstPlusLength([1,2,3,4,5]))
print('======================================')

# ! Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

def values_greater_than_second(a_list):
    arr = []
    for i in range(len(a_list)):
        if a_list[1] > a_list[1]:
            arr.append(a_list[i])
        print(len(arr))
        return arr

print(values_greater_than_second([5,2,7,1,2,3,4,5]))
print('======================================')

# ! This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def this_length_that_value(size,value): #Write a function that accepts two integers as parameters: size and value.
    arr = [] #Create a list
    for i in range(0, size): #Loop dictates how many times to run and append dictates how big the list will be
        arr.append(value) #appening given value
    return arr #return a list


print(this_length_that_value(5,7)) #[7,7,7,7,7]