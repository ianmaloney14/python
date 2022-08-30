x = [ [5,2,3], [10,8,9] ]
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'},
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x[1][0])

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y'] = 30
print(z)

def iterateDictionary(some_list):
    for key in range(len(some_list)):
        print("first_name - "+some_list[key]['first_name']+", last_name - "+some_list[key]['last_name'])
iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for key in range(len(some_list)):
        print(some_list[key][key_name])

print(iterateDictionary2('first_name', students))
print(iterateDictionary2('last_name', students))

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key)
        for i in range(len(some_dict[key])):
            print(some_dict[key][i])
        print("")

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
