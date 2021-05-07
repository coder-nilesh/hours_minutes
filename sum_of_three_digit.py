'''Given three digit intiger.Find the sum of its digit'''
n=int(input("Enter the three digit number:"))
s=0
b=0
while(n!=0):
    b=b+(n%10)
    n=n//10

print(b)
