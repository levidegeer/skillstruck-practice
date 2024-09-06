number = int(input())
arr = []
for x in range(2, number):
    a = int(number / x)
    if number / x == a:
        arr.append(x)
if len(arr) == 0:
    print(str(number) + " is a prime number")
else:
    print(arr)
        
    