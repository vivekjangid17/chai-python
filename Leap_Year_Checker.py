# 9. Leap Year Checker
#     - Determine if a year is a leep year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year = int(input("Enter any year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"Year {year} is a leap year.")
else:
    print(f"Year {year} is not a leap year.")
    