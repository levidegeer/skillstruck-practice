# var1 = "1"
# var2 = "2"
# var3 = "3"
# print(var1)
# print(var2)
# print(var3)

# how_much_wood_would_a_wood_chuck_chuck_if_a_wood_chuck_could_chuck_wood = 5
# print(how_much_wood_would_a_wood_chuck_chuck_if_a_wood_chuck_could_chuck_wood)

def reverse_words(s):
    lst = s.split()
    lst2 = []
    string = ""
    for x in lst:
        lst2.insert(0, x)
    for x in lst2:
        string = string + " " + x
    print(string)

reverse_words("Hello world!")

