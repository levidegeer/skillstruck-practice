word_lst = ["For", "this", "project", "you", "will", "create", "list", "of", "words", "which", "will"]
number = int(input())
word = word_lst[number]
word_l = []
word_l.extend(word)
turns = 12
while turns > 0:
    myletter = input()
    print("")
    for x in word_l:
        if myletter == x:
            print(myletter)
        else:
            print("-")
    turns -= 1

print("You ran out of turns")