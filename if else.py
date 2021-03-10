'''Price of a house is $1M.If buyer has good credit,
they need to put down 10% other wise they need to put down 20%
print the down payment'''
#
#
# price = 1000000
# good_credit = True
#
# if good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
#
# print(f"down_payment : ${down_payment}")

'''if  temperature is greater than 30,it's a hot day other wise  if it's less than 10;
it's a col'd other wise it is nither hot nor cold'''


# temp =int(input("Enter the temperature:"))
#
# if temp >30:
#     print("it's a hot day")
# elif temp < 10:
#     print("it's a cold day")
# else:
#     print("it's nither hot nor cold")
#
#


'''
Weight Converter: 
input the weight of a person in either kg or lbs.
if the person provides his/her weight in kg
then convert it into lbs else convert it to kg
'''

weight = int(input("Enter the Weight of the person:"))
a = input(" kg or lbs")

if a == "kg":
    convert_kg = weight / 0.45
    print(f"the person weight is {convert_kg} pounds")
elif a == "lbs":
    convert_lbs = weight * 0.45
    print(f"the person weight is {convert_lbs} kilos ")
else:
    print(f"please enter the appropriate character  kg or  lbs!")















