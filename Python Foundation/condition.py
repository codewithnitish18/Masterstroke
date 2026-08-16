# number = int(input("enter a number:"))
# if(number >= 0):
#     print("postive number")
# else:
#     print("negative number")



# age = int(input("enter your age:"))
# if(age>18):
#     print("you are eligible for voting")
# else:
#     print("you are not eligible for voting")




# a =25
# b =25
# c =17
# if(a>=b and a>=c):
#     print("a is greater number", a)
# elif(b>=c and b>=a):
#     print("b is a greater number", b)
# else:
#     print("c is the greater number", c)

units = int(input("Enter the units you consumed:"))
if(units <= 100):
    bill1 = units * 5
elif(units>100 and units<=200):
    bill2 = (units * 5) + ((units - 100) * 7)
else:
    bill3 = units * 10
print ("total bill is:", bill1 + bill2 + bill3)         
