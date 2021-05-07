'''Check wheather the given year is leap year or not.if year is leap print "LEAP YEAR"
else print "COMMON YEAR"
Hint:a year is a leap year if its number is exactly divisible by 4 and it is not'''
year = int(input("Enter the year:"))
if year%4==0:
    print("The  given year is leap year")
else:
    print("The given year is comman year")