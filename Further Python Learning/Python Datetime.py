import datetime

# x = datetime.datetime.now()
# today = datetime.date.today()
# print(x)
# print(today)
# print(x.strftime("%X"))
# print(x.strftime("%d"))
# print(today.strftime("%m"))
# print(today.strftime("%Y"))

# birth_day_month = int(input("What is your birthday month? "))
# x = datetime.datetime.now()
# today = datetime.date.today()
# current_day = x.strftime("%d")
# current_month = today.strftime("%m")
# months_till = birth_day_month - int(current_month)
# if months_till < 0:
#     months_till = 12 + months_till
# months_till = months_till - 1
# months = birth_day_month - 1
# if months == 4 or months == 6 or months == 9 or months == 11:
# 	days_left = (30 - int(current_day))
# elif months == 2:
#     days_left = (28 - int(current_day))
# else:
#     days_left = (31 - int(current_day))
# print("You have " + str(months_till) + " months and " + str(days_left) + " days until it's your birthday month!")

# x = datetime.datetime.now()
# current_month = x.strftime("%m")
# current_day = x.strftime("%d")
# months_since = int(current_month) - 1
# days_since = int(current_day) - 1
# print("It has been " + str(months_since) + " months and " + str(days_since) + " days since your New Years resolution. How are you doing?")

# x = datetime.datetime.now()
# current_year = x.strftime("%Y")
# years_since = int(current_year) - 1972
# print("It has been " + str(years_since) + " years since the first computer program ever. Look how far we have come!")

# x = datetime.datetime.now()
# current_year = x.strftime("%Y")
# time = int(current_year) - 2020
# calculation = time % 4
# if calculation == 0:
#     print("This year " + str(current_year) + ", is a leap year")
# else:
#     print("This year " + str(current_year) + ", is not a leap year")

x = datetime.datetime.now()
month = int(x.strftime("%m"))
if month == 1:
    print("It is Jan")
elif month == 2:
    print("It is Feb")
elif month == 3:
    print("It is Mar")
elif month == 4:
    print("It is Apr")
elif month == 5:
    print("It is May")
elif month == 6:
    print("It is Jun")
elif month == 7:
    print("It is Jul")
elif month == 8:
    print("It is Aug")
elif month == 9:
    print("It is Sep")
elif month == 10:
    print("It is Oct")
elif month == 11:
    print("It is Nov")
else:
    print("It is Dec")
