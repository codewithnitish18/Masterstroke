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

# units = int(input("Enter the units you consumed:"))
# if(units <= 100):
#     bill = units * 5
# elif(units<=200):
#     bill = (100 * 5) + ((units - 100) * 7)
# else:
#     bill = (100*5) + (100*7) + (units - 200) * 10
# print ("total bill is:", bill)         


a = int(input("Enter a side 1:"))
b = int(input("Enter a side 2:"))
c = int(input("Enter a side 3:"))

if(a+b>c and b+c>a and a+c>b):
    print("Valid triangle")
else:
    print("invalid triangle")

