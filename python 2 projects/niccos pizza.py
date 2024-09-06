people = int(input("Number of people = "))
large = people // 7
remaining = people - large * 7
medium = remaining // 3
remaining = remaining - medium * 3
small = remaining // 1
print("You will need " + x + " large pizzas, " + x + " medium pizzas, and " + x + " small pizzas.")
