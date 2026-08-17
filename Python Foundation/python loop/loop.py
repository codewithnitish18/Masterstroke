# loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. The code inside the loop will continue to execute as long as the condition is true. There are two main types of loops in Python: for loops and while loops.
#for looop is used to iterate when we know the how many times you want to repeat something or you are going through a sequence of things
# i is simply a variable that gets a value on each iteration
#one execution of the loop is called an iteration


number = int(input("Enter a number:"))
print("the number is:", number)
total = 0
while number > 0:
    digit = number % 10
    total = total + digit
    number = number // 10
print(total)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for number in numbers:
    if number % 2 == 0:
        count += 1
    
print("the count of even numbers is : ", count)



number = int(input("Enter a number:"))
count = 0
while number > 0:
    digit = number % 10
    if digit % 2 == 0:
        count += 1
    number = number // 10
print("the count of even digits is :", count)









number = int(input("Enter a number:"))
even_count = 0
odd_count = 0
total = 0
while number > 0:
    digit = number % 10
    total = total + digit
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    number = number // 10
print("the count of even digits is:", even_count)
print("the count of odd digits is:", odd_count)
print("the total of all digits is:", total)