# var = "test"
# try:
#     print(var)
# except:
#     print("test2")
# else:
#     print("test3")
# finally:
#     print("test4")

# s = int(input("Number of slices = "))
# p = int(input("Number of people = "))
# try:
#     print(s/p)
# except:
#     print("Your code doesn't account for if a user tries to enter 0 people")
# else:
#     print("There is no problem")
# finally:
#     print("Your exception handling is complete")

# sunflowers = int(input("How many sunflowers? "))
# try:
#     print(sunflowers * 300)
# except:
#     print("There is a problem")
# else:
#     print("There is no problem")
# finally:
#     print("Your exception handling is complete")

a = input("What is the color of your shirt? ")
b = input("What object is closest to your ear right now? ")
c = input("What object is closest to your elbow right now? ")
d = input("What were you doing at 5pm yesterday? ")
e = int(input("How many pairs of socks do you own? "))

try:
    print(a + b + c + d + str(e * 10))
except:
    print("User entered an invalid number")
else:
    print("There is no problem")
finally:
    print("Your exception handling is complete")