# Hello! Thank you for taking time to review my work. This task requires me to design a program that determines the award a person competing in a triathlon will receive

# Firstly I ask the program to print "Triathlon Award Results so the person competing is aware of the parameters for the type of award they receive "
print("          ")
print("This is Triathlon Results Award which will produce your award based on the time you achieved for each sporting activity.")
print("          ")

# Secondly I defined the total_triathlon_time using the three sporting actvities which will give the total time
def calculate_award(swim_time, cycle_time, run_time):
    total_triathlon_time = swim_time + cycle_time + run_time

# Thirdly I use the 'or' operator to bring logic and I also used comparison operator within the programme to present the award output based on the input time
    if total_triathlon_time <= 100:
        return "Congratulations you have been awarded Provincial Colours"
    elif total_triathlon_time == 101 or total_triathlon_time <= 105:
        return "Congratulations you have been awarded Provincial Half Colours"
    elif total_triathlon_time == 106 or total_triathlon_time <= 110:
        return "Congratulations you have been awarded Provincial Scroll"
    else:
        return "Unfortunately you have no award due to not meeting the qualifying time criteria"

#The user will input their triathlon times directly and get the award
swim_time = float(input("Please enter your achieved swimming time in minutes only (minutes): "))
cycle_time = float(input("Please enter your achieved cycling time in minutes only (minutes): "))
run_time = float(input("Please enter your achieved running time in minutes only (minutes): "))

award = calculate_award(swim_time, cycle_time, run_time)
print(f" {award}")
