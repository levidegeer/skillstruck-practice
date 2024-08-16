# rows = 3
# pets = ["dog", "cat", "fish", "rabbit", "bird"]
# my_list = [[a for a in pets] for i in range(rows)]
# print(my_list)

# rows = int(input("How many rows? "))
# my_list = [1, 2, 3, 4, 5]
# end_list = [[a*rows for a in my_list] for i in range(rows)]
# print(end_list)

# weather = input("Input a list of weather ").split()
# cols = ["windy", "breezy", "calm"]
# b = []
# for x in weather:    
#     a = []
#     for y in cols:
#         w = x + " " + y
#         a.append(w)
#     b.append(a)
# print(b)

# rows = 5
# cols = 3
# list = []
# for x in range(rows):
#     other_list = []
#     for y in range(cols):
#         other_list.append(y)
#     list.append(5)
# print(list)

# first_names = ["a" , "b", "c", "d"]
# last_names = ["a" , "b", "c", "d"]
# list = []
# for x in first_names:
#     other_list = []
#     for y in last_names:
#         other_list.append(x + " " + y)
#     list.append(x)
# print(list)

# first = input("Input a list of fruits").split()
# last = ["apple", "grape", "peach", "cinnamon", "vanilla"]
# list = []
# for x in first:
#     other_list = []
#     for y in last:
#         other_list.append(x + " " + y)
#     list.append(other_list)
# print(list)

# first = [int(n) for n in input("Input a list of numbers").split()]
# last = [2, 5, 10, 100]
# list = []
# for x in first:
#     other_list = []
#     for y in last:
#         other_list.append(x - y)
#     list.append(other_list)
# print(list)

arr_val = [1000, 1000, 100]
arr_unit = ["g", "kg", "m"]


def solution(arr_val, arr_unit) : 
    if arr_unit[0] == "kg":
        first_mass == arr_val[0]
    elif arr_unit[0] == "g":
        first_mass = arr_val[0] / 1000
    elif arr_unit[0] == "mg":
        first_mass = arr_val[0] / 1000000
    elif arr_unit[0] == "μg":
        first_mass = arr_val[0] / 1000000000
    elif arr_unit[0] == "lb":
        first_mass = arr_val[0] / 2.204623
    
    if arr_unit[1] == "kg":
        second_mass = arr_val[1]
    elif arr_unit[1] == "g":
        second_mass = arr_val[1] / 1000
    elif arr_unit[1] == "mg":
        second_mass = arr_val[1] / 1000000
    elif arr_unit[1] == "μg":
        second_mass = arr_val[1] / 1000000000
    elif arr_unit[1] == "lb":
        second_mass = arr_val[1] / 2.204623
    
    if arr_unit[2] == "m":
        distance = arr_val[2]
    elif arr_unit[2] == "cm":
        distance = arr_val[2] / 100
    elif arr_unit[2] == "mm":
        distance = arr_val[2] / 1000
    elif arr_unit[2] == "μm":
        distance = arr_val[2] / 1000000
    elif arr_unit[2] == "ft":
        distance = arr_val[2] / 3.28084


    f = (6.67e-11) * first_mass * second_mass / (distance**2)
    print(f)  

solution(arr_val, arr_unit)


















































