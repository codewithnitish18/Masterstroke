# numbers = [7,12,4,19,8]
# largest = numbers[0]
# for number in numbers:
#     if number > largest:
#         largest = number
# print("the largest number is:", largest)


# numbers = [2,5,7,19,12,19]
# largest = numbers[0]
# second_largest = numbers[1]
# if numbers[1] > numbers[0]:
#     largest = numbers[1]
#     second_largest = numbers[0]
# else:
#     largest = numbers[0]
#     second_largest = numbers[1]

# for number in numbers[2:]:
#     if number > largest:
#         second_largest = largest
#         largest = number
#     elif number > second_largest:
#      second_largest = number
# print("first and second largest numbers are:", largest, second_largest)






# numbers = [2,]
# if len(numbers) < 2:
#     print("there is no second largest numbers in the list..")
# else:
#     largest = numbers[0]
#     second_largest = numbers[1]

#     if numbers[1] > numbers[0]:
#         largest = numbers[1]
#         second_largest = numbers[0]
#     else:
#         largest = numbers[0]
#         second_largest = numbers[1]

#     for number in numbers[2:]:
#         if number > largest:
#             second_largest = largest
#             largest = number
#         elif number > second_largest:
#             second_largest = number
#             print("laregst number is:", largest)
#             print("second largest number is:", second_largest)


arr = [1,2,4,6,9]
target = 4
low = 0
high = len(arr) - 1 

while(low <= high):
    mid = (low + high)//2
    if arr[mid] == target:
        print(f'target found at the index {mid}')
        break
    elif arr[mid] < target:
        low = mid + 1
    elif arr[mid] > target:
        high = mid - 1
else:
  print("Number not found")