# string = "test {} test {}"
# integer = 56
# print(string.format(integer, integer))

# x = input()
# total = int(x[0]) + int(x[1]) + int(x[2])
# string = "The sum of those digits is {}"
# print(string.format(total))

# mpd = int(input())
# tnm = int(input())
# print("The total number of days you will need to drive there is " + str(tnm/mpd))

# x = str(input())
# a = x.find(".")
# print("The first decimal digit is " + x[a+1])

# dollars = int(input("Dollars "))
# cents = int(input("Cents "))
# cookies = int(input("Cookies "))
# cents = cents/100
# price = dollars + cents
# total = cookies * price
# print("The total cost of " + str(cookies) + " cookies is $" + str(total))

number = int(input())
number = number + 3
if number > 6:
    number = number % 7
print("The day of the week is the number " + str(number))




