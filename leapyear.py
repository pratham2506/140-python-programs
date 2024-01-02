year = int(input("Enter the year : "))
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
    
    
























# The concept of leap years is a way to adjust the calendar to keep it synchronized with the astronomical year. The basic rule for determining a leap year is that it is evenly divisible by 4, which means it has 366 days instead of the usual 365. However, to maintain accuracy, an exception is made for century years (years ending with 00).

# Here are the rules explained:

# Divisible by 4: If a year is evenly divisible by 4, it is a leap year. For example, the years 2004, 2008, and 2012 are leap years because they are divisible by 4.

# Exception for Century Years: Century years (years ending with 00) are a special case. Not all century years are leap years. To be a leap year, a century year must also be divisible by 400.

# Rule for Century Years: If a century year is divisible by 400, it is a leap year. For example, the years 1600 and 2000 are leap years because they are divisible by both 100 and 400.

# Exception for Century Years Not Divisible by 400: If a century year is not divisible by 400, it is not a leap year. For example, the years 1700, 1800, and 1900 are not leap years because, although they are divisible by 4 and 100, they are not divisible by 400.