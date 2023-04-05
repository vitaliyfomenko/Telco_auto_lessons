# 1
john_salary = 2.5
marta_salary = 3.5
print(john_salary)
print(marta_salary)
print("------------------------------")

# 2
john_age = 23
marta_age = 32
print(john_age)
print(marta_age)
print("------------------------------")

# 3
john_name = "John"
marta_name = "Marta"
print(john_name)
print(marta_name)
print("------------------------------")

# 4
john_gender = False
marta_gender = True
print(john_gender)
print(marta_gender)
print("------------------------------")

# 5
john_friends = ["bob", "james"]
marta_friends = ["jeniffer", "amanda"]
print(john_friends)
print(marta_friends)
print("------------------------------")

# 6
list_of_names = ["bob", "james", "bob", "amanda"]
print(list(set(list_of_names)))
print("------------------------------")

# 7
john_coordinates = (44.4268, 26.1025)
marta_coordinates = (45.4268, 27.1025)

# 8
john = {
    "Full_name": john_name,
    "Age": john_age,
    "Salary": john_salary,
    "Gender": john_gender,
    "Friends": john_friends,
    "Coordinates": john_coordinates
}

marta = {
    "Full_name": marta_name,
    "Age": marta_age,
    "Salary": marta_salary,
    "Gender": marta_gender,
    "Friends": marta_friends,
    "Coordinates": marta_coordinates
}

for a, b in john.items():
    print(str(a) + " => " + str(b))
print("------------------------------")

for a, b in marta.items():
    print(str(a) + " => " + str(b))
print("------------------------------")

# challenge
john_friends_2 = [{
    "Full_name": "bob",
    "Age": 7,
    "Salary": 10.55,
    "Gender": True,
    "Friend": ["john", "adam"],
    "Coordinates":(44.4268, 26.1025)
},
{
    "Full_name": "alfred",
    "Age": 10,
    "Salary": 10.81,
    "Gender": False,
    "Friend": ["john", "justin"],
    "Coordinates":(45.4268, 27.1025)
}
]

for x in john_friends_2:
    for a, b in x.items():
        print(str(a) + " => " + str(b))
print("------------------------------")

marta_friends_2 = [{
    "Full_name": "albina",
    "Age": 15,
    "Salary": 35.58,
    "Gender": True,
    "Friend": ["marta", "dana"],
    "Coordinates":(40.4268, 36.1025)
},
{
    "Full_name": "jill",
    "Age": 45,
    "Salary": 10.01,
    "Gender": True,
    "Friend": ["lily", "stella"],
    "Coordinates":(12.4268, 15.1025)
}
]

for x in marta_friends_2:
    for a, b in x.items():
        print(str(a) + " => " + str(b))

