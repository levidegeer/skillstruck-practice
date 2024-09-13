# caterpillars = 3
# leaves = 25
# print(caterpillars*leaves)

# num1 = int(input("What is your first number?"))
# num2 = int(input("What is your second number?"))
# print(num1 + num2)

# num1 = int(input())
# print(str(num1-1) + "," + str(num1+1))

# num1 = int(input("Number of people "))
# num2 = int(input("Money per person "))
# print(num1 * num2)

# inheritance_amount = 48682.76
# people = int(input("Number of people "))
# print("If " + str(people) + " people split the inheritance, each person would get " + str(inheritance_amount/people) + " dollars.")

# year = int(input())
# century = year // 100
# print(century+1)

num_people = int(input("How many people are coming to dinner? "))
num_people = num_people

hamburger_price = 1.29
rolls_price = 0.49
corn_price = 0.80

hamburger_count = int(input("How many hamburgers will everyone have? "))
rolls_count = int(input("How many rolls will everyone have? "))
corn_count = int(input("How many pieces of corn will you have? "))

total = 0
total = total + (hamburger_count * hamburger_price * num_people)
total = total + (rolls_count * rolls_price * num_people)
total = total + (corn_count * corn_price * num_people)

noChange = int(total / num_people)
change = float(total / num_people)
print("Each person owes $" + str(noChange) + " without change, or $" + str(change) + " if change is included.")