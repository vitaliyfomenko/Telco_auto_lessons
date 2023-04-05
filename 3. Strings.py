# 1
import string
string_names = "john peter brian Morgan Adam Maria bart"
print(string.capwords(string_names))
print("------------------------------")

# 2
list_of_friends = ["John", "Marta", "James", "Amanda", "Marianna"]
txt = "Names"
new_txt = txt.center(20, "*")
print(new_txt)
for name in list_of_friends:
    print(f"{name:>20}")
print("------------------------------")

# 3
base_string = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
string_no_space = base_string.strip()
string = string_no_space.replace("&", " ").replace("=sssss", " ").replace("  ", " ").replace(" ", ";")
list_str = string.split(";")
dict_str = dict(x.split("=") for x in list_str)
print(dict_str)
print("------------------------------")

# 4
list_names = ["FirstItem", "FriendsList", "MyTuple"]
result = ""
for item in list_names:
    for i in item:
        if i.isupper():
            result = result + "_" + i.lower()
        else:
            result = result + i
print(result)

