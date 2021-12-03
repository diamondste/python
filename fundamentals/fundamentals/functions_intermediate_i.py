#1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
def update(x):
    x[1][0] = 15
    return x
a = update(x)
print(a)

#2. Change the last_name of the first student from 'Jordan' to 'Bryant'
def changeName(students):
    students[0]['last_name'] = 'Bryant'
    return students

b = changeName(students)
print(b)

#3 In the sports_directory, change 'Messi' to 'Andres'
def updateSports(sports):
    sports['soccer'][0] = 'Andres'
    return sports

h = updateSports(sports_directory)
print(h)

#4 Change the value 20 in z to 30
def changeNum(z):
    z[0]['x'] = 30
    return z

i = changeNum(z)
print(i)

#2. Iterate Through a List of Dictionaries
student = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for x in some_list:
        for key, val in x.items():
            print("{} - {}".format(key, val) )

iterateDictionary(student)

#3 Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for x in some_list:
        for key, val in x.items():
            if key == key_name:
                print("{}".format(val))

iterateDictionary2('first_name', student)

#4 Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
        for key in some_dict:
            value = some_dict[key]
            key_len = len(key)
            print(key_len, key, value)
printInfo(dojo)
