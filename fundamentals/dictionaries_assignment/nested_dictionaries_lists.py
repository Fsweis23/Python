x = [ [5,2,3], [10,8,9] ] 

students = [
    {'first_name':  'Michael', 'last_name' : 'Bryant'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 15, 'y': 30} ]

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# iterateDictionary(students) 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# def iterate_dictionary(some_list):
#     for i in range(len(some_list)):
#         empty_str = ""
#         for key, val in some_list[i].items():
#             empty_str+= f"{key}-{val},"
#         print(f"{empty_str}")

def iterateDictionary(students):
    for i in range(len(students)):
        output = ''
        for key, value in students [i].items():
            print(f'{key} = {value}, ')

iterateDictionary(students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    # print(f'{len(dojo)}'):
    # for i in range(0,len(arr[]):
        
    #   print(arr[1])
    for key, value in dojo.items():
        print(len(value), key.upper())
        for i in range(0, len(value)):
            print(value[i])
    
    printInfo(dojo)