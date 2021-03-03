"""A  school decided to replace the desk in three  class room.
Each desk sits two student.Given the number of students in each class, print the smallest
possible number of desks thet can be purchased.
The program should read three integers: the number of student in each of the three classes,a,b and  c
respectively.
In the first test there are three groups. The first group has 20 student  and thus needs 10 desk.
the second group has 21 student,so they can get """
first_class = int(input("Enter the number of desk in first class"))
second_class = int(input("Enter the number of desk in second class"))
third_class = int(input("Enter the number of desk in third class"))
total_student = first_class+second_student+third_class
no_of_desk = total_student//2
remaining = total_student%2
least_number_of_desk = number_of_desk+remaining
print(f"the least no of desk required is {least_number_of_desk}")







