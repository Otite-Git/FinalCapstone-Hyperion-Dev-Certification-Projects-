import math
# Hello, Thank you for taking time to review my work. The first activity requires me to write a code that allows a user to between and investment or bond calculation.""

# I created the menu option using the print() 
print ("  ")
print("Hello! Thank you for using the financial calculator.")
print("__________________________________________________\n")

print("Menu Options:")
print("investment - to calculate interest on investment")
print("bond       - to calculate bond repayment")
choice = input("Enter 'investment' or 'bond' to proceed: ").lower()

# I use the comparison operator and reusable code function to define the variable. Integer and float is used to capture numbers with and without decimals points
if choice == "investment":
    deposit = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of years for investment: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

# If, Else & Elis statements used to catpture the input from the user. Depending on the input above, the statement will generate the simple or compunt type calculation. 
    r = interest_rate / 100
    if interest_type == "simple":
        total_amount = deposit * (1 + r * years)
    elif interest_type == "compound":
        total_amount = deposit * math.pow((1 + r), years)
    else:
        print("Invalid interest type entered. Please choose 'simple' or 'compound'.")
        total_amount = None

    if total_amount is not None:
        print(f"Total amount after {years} years: {total_amount:.2f}")

elif choice == "bond":
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate: "))
    months = int(input("Enter the number of months for bond repayment: "))

    i = (interest_rate / 100) / 12
    repayment = (i * present_value) / (1 - (1 + i) ** (-months))

    print(f"Monthly bond repayment: {repayment:.2f}")

else:
    print("Invalid option. Please enter 'investment' or 'bond'.")
