'''WAP which accepts marks of four subject and display total marks,percentages and grade.
Hint: more than 70% ->distinction,morethan 60% -> first,more tha 40% ->pass less than 40% ->fail'''
english = int(input("Enter the marks of English:"))
math = int(input("Enter the marks of math:"))
nepali = int(input("Enter the marks of Nepali:"))
social_studies = int(input("Enter the marks of social studies:"))
total_marks = english+math+nepali+social_studies
print(f"Total marks is {total_marks}")
percentage = (total_marks/400)*100
print(f"your percentages is{percentage}")
if percentage >=70:
    print(f"Congratulation You scored distinction.Keep it up.")
elif percentage >=60:
    print(f"Congratulation you scored first division.Keep it up.")
elif percentage >=40:
    print(f"you are passed.You Need to work hard")
else:
    print(f"you are fail Idiot.")