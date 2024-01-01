# This task requirments me to generate a program that will be used to output a variety of responses determined by the data users entry

# If the user is 40 or over, output the message "You're over the hill."
# For this I firstly define the age variable using the integer data type
age = int(input("What is your age?"))


#Secondly, I use the 'if' Statement to establish whether the number entered is greater than 100 using if age > 100, output the message "Sorry you're dead"
if age > 100:
    print("sorry you're dead")

#Thirdly, I use the 'elif' Statement below to establish whether the number entered is greater than or equal to 65 using elif age >= 65, output the message "Enjoy your retirement"
elif age >= 65:
    print("Enjoy your retirement") 
    
#If the user is 40 or older using elif age >= 40, output the message "You're over the Hill!" elif 
elif age >= 40:
   print("You're over the hill.") 

#If If the user is 21 using elif age == 21, output the message "Congrats on your 21st!"
elif age == 21:
    print("Congrats on your 21st!")

#If the user is under 13, output the message using elif age < 13, output the message "You qualify for the kiddie discount."
elif age < 13:   
    print("You qualify for the kiddie discount.")

# For any other age using 'else:' output the message "Age is but a number."
else: 
    print("Age is but a number")

