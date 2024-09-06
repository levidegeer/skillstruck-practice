# User input
earningsgoal = int(input("How much money do you want to save in a year?: "))

# Performs calculation
months = earningsgoal / 12
weeks = earningsgoal / 52
days= earningsgoal / 365

# Prints the result
print("In order to save " + str(earningsgoal) + " in one year. You need to save:")
print(str(round(months, 2)) + " Monthly")
print(str(round(weeks, 2)) + " Weekly")
print(str(round(days, 2)) + " Daily")