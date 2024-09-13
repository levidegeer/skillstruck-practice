my_lst = ["For", "this", "project", "you", "will", "create", "list", "of", "words", "which", "will"]
number = int(input())
word = my_lst[number]
lst = list(word)
turns = 12
while turns > 0:
    myletter = input("Input a letter")
    if myletter in lst:
        print(myletter)
    else:
        print("-")
    turns -= 1

