'''Write a python program to converts seconds to day, hour,minutes.'''
seconds = int(input("Enter the seconds:"))
minutes = seconds/60
hours = seconds/(60*60)
days = seconds / (60*60*24)
print(f"The converted number of minutes is {minutes}")
print(f"The converted number of hours is {hours}")
print(f"The converted number of days is {days}")
