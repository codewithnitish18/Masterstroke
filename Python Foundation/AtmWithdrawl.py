# The user enters:

# balance
# withdrawal_amount

# The withdrawal should be allowed only if:

# Withdrawal amount is greater than 0
# Withdrawal amount is less than or equal to balance
# Withdrawal amount must be a multiple of 100

balance = int(input("Enter the Balance:"))
withdrawlamt = int(input("enter the amount you want to withdrawl:"))
if((withdrawlamt >0) and (withdrawlamt<=balance) and (withdrawlamt % 100 == 0)):
    print("Withdrawal successfull")
    remaining_amount = balance - withdrawlamt
    print(remaining_amount)
else:
    print("invalid withdrwal")