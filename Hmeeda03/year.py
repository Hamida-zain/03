year=int(input("Enter a year: "))
if (year % 4 == 0) and (year % 100 == 0):
    print (year, "it's not a leap year")
elif (year % 400 == 0) and (year % 100 != 0):
    print (year, "it's a leap year")
else:
    print(year, "it's not a leap year")