answer = "y"
arr = []
while answer == "y":
    answer = input()
    if answer == "y":
        name = input()
        arr.append(name)
    else:
        pass
arr.sort()
print(arr)
