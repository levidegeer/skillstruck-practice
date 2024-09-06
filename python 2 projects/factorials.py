number = int(input())
c = 0
for x in range(1, number+1):
    t = 1
    for y in range(1, x+1):
        t = t * y
    c = c + t
print(c)