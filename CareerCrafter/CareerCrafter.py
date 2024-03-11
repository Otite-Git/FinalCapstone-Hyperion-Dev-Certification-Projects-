# Hi in this project I have developed a program that validates the personal data of a user's application.
# This progam uses definsive programming to ensure the user inpur is valid:
   # Using conditional statements for input validation.
   # Usage of try-excep blocks errors to effciently manage unexpected  exceptions.
   # Recognise and address various error types.



from tabulate import tabulate

def separator():
    print("=" * 100)

print("\n")
separator()
print("Hi there! In order to successfully complete your application form, kindly follow the steps below: ")
separator()
print("\n")

# Validates whether firstname and surname have been provided
while True:
    user_name = input("Please enter your first name and surname: ")
    names = user_name.split(' ')
    if len(names) >= 2:
        first_name = names[0]
        surname = ' '.join(names[1:])
        full_name = first_name.capitalize() + ' ' + surname.capitalize()
        print(f"Your full name is {full_name}.")
        break
    else:
        print("Please enter both your first name and surname")
        print("\n")

print("\n")
while True:
    user_email = input("Please enter your email address: ")
    if "@" in user_email and "." in user_email:
        print(f"The applicant's email address is {user_email}.")
        break
    else:
        print("The applicant has an invalid email address")
        print("\n")

print("\n")
while True:
    user_contact_number = input("Please enter your contact number: ")
    if len(user_contact_number) == 11 and user_contact_number.isnumeric():
        print(f"The applicant's contact number is {user_contact_number}.")
        break
    else:
        print("The applicant has an invalid contact number")
        print("\n")

while True:
    try:
        print("\n")
        user_age = input("Please enter your age: ")
        user_age = int(user_age)
        if user_age >= 0:
            print(f"The applicant is {user_age} years old.")
            break
        else:
            print("Please enter a non-negative age.")
            print("\n")
    except ValueError:
        print("The applicant's age contains invalid characters.")

while True:
    try:
        print("\n")
        nationality = input("Please enter your nationality: ")
        if nationality.isalpha():
            cap_nationality = nationality.capitalize()
            print(f"Your nationality is {cap_nationality}.")
            print("\n")
            break
        else:
            print("Please enter a valid nationality")
            print("\n")
    except ValueError:
        print("\n")
        print("The applicant's nationality contains invalid characters.")
        print("\n")

user_information = [
    ["Full Name", full_name],
    ["Email Address", user_email],
    ["Contact Number", user_contact_number],
    ["Age", user_age], 
    ["Nationality", cap_nationality],
]
print("\n")

# Printing collected information in a table
print("Thank you for providing your infomration, Here is a summary table below:")
print("\n")
print(tabulate(user_information, headers=["Field", "Information"], tablefmt="grid"))
print("\n")






    
