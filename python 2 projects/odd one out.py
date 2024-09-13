my_list = input().split()
dct = {}
for x in my_list:
    y = x[0]
    if y not in dct:
        dct[y] = 1
    else:
        dct[y] += 1
t = 0
for x,y in dct.items():
    if y > t:
        t = y
        result = x
string = ""
for x in my_list:
    if x[0] == result:
        string = string + " " + x
print(string.strip())
