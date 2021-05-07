'''Given three integers,print the smallest one.(Three intigers shouled be intered by users)'''

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a<b and a<c:
    print(f"The number {a} is the smallest number")
elif b<a and b<c:
    pirnt(f"The number {b} is the smallest number")
else:
    print(f"The number {c} is the smallest number")
    