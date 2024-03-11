import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Function to register a new user
def reg_user(username_password):
    print("=" * 40)
    new_username = input("New Username: ")
    if new_username in username_password.keys():
        print("Username already exists. Please choose a different username.")
        return

    new_password = input("New Password: ")
    confirm_password = input("Confirm Password: ")

    if new_password == confirm_password:
        print("New user added")
        username_password[new_username] = new_password
        with open("user.txt", "w") as out_file:
            user_data = [f"{k};{username_password[k]}" for k in username_password]
            out_file.write("\n".join(user_data))
    else:
        print("Passwords do not match")

# Function to add a new task
def add_task(task_list, username_password):
    print("=" * 40)
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username.")
        return
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    curr_date = date.today()
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")

# Function to view all tasks
def view_all(task_list):
    print("=" * 40)
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)

# Function to view tasks assigned to the current user
def view_mine(task_list, curr_user):
    task_number = 1
    print("=" * 40)
    for t in task_list:
        if t['username'] == curr_user:
            disp_str = f"{task_number}. Task: \t\t {t['title']}\n"
            disp_str += f"   Assigned to: \t {t['username']}\n"
            disp_str += f"   Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"   Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"   Task Description: \n {t['description']}\n"
            print(disp_str)
            task_number += 1

    task_selection = input("Enter the task number to edit, or enter -1 to return to the main menu: ")

    try:
        task_selection = int(task_selection)
        if task_selection == -1:
            return

        selected_task = task_list[task_selection - 1]
        if not selected_task['completed']:
            action = input("Enter 'c' to mark the task as complete or 'e' to edit the task: ").lower()
            if action == 'c':
                selected_task['completed'] = True
                print("Task marked as complete.")
            elif action == 'e':
                new_username = input("Enter the new username (leave empty to keep current): ")
                new_due_date = input("Enter the new due date (YYYY-MM-DD, leave empty to keep current): ")

                if new_username:
                    selected_task['username'] = new_username
                if new_due_date:
                    selected_task['due_date'] = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)

                print("Task edited successfully.")
        else:
            print("Cannot edit a completed task.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Function to generate reports
def generate_reports(task_list, username_password):
    # Task overview
    total_tasks = len(task_list)
    completed_tasks = sum(1 for t in task_list if t['completed'])
    uncompleted_tasks = total_tasks - completed_tasks

    # Calculate overdue tasks
    today_date = date.today()
    overdue_tasks = sum(1 for t in task_list if not t['completed'] and t['due_date'].date() < today_date)

    # User overview
    total_users = len(username_password)
    tasks_per_user = {user: sum(1 for t in task_list if t['username'] == user) for user in username_password}
    tasks_completed_per_user = {user: sum(1 for t in task_list if t['username'] == user and t['completed']) for user in username_password}

    # Generate task overview report
    with open("task_overview.txt", "w") as task_overview_file:
        task_overview_file.write("=" * 40 + "\n")
        task_overview_file.write("Task Overview Report\n")
        task_overview_file.write("=" * 40 + "\n\n")
        task_overview_file.write(f"Total tasks: {total_tasks}\n")
        task_overview_file.write(f"Completed tasks: {completed_tasks}\n")
        task_overview_file.write(f"Uncompleted tasks: {uncompleted_tasks}\n")
        task_overview_file.write(f"Overdue tasks: {overdue_tasks}\n")
        task_overview_file.write(f"Percentage of tasks incomplete: {uncompleted_tasks / total_tasks * 100:.2f}%\n")
        task_overview_file.write(f"Percentage of tasks overdue: {overdue_tasks / total_tasks * 100:.2f}%\n")

    # Generate user overview report
    with open("user_overview.txt", "w") as user_overview_file:
        user_overview_file.write("=" * 40 + "\n")
        user_overview_file.write("User Overview Report\n")
        user_overview_file.write("=" * 40 + "\n\n")
        user_overview_file.write(f"Total users: {total_users}\n")
        user_overview_file.write(f"Total tasks: {total_tasks}\n\n")

        for user in username_password:
            tasks_assigned = tasks_per_user[user]
            percentage_of_total_tasks = tasks_assigned / total_tasks * 100 if total_tasks > 0 else 0
            percentage_of_completed_tasks = (tasks_completed_per_user[user] / tasks_assigned * 100) if tasks_assigned > 0 else 0

            user_overview_file.write("=" * 40 + "\n")
            user_overview_file.write(f"User: {user}\n")
            user_overview_file.write("=" * 40 + "\n")
            user_overview_file.write(f"Tasks assigned: {tasks_assigned}\n")
            user_overview_file.write(f"Percentage of total tasks: {percentage_of_total_tasks:.2f}%\n")
            user_overview_file.write(f"Percentage of completed tasks: {percentage_of_completed_tasks:.2f}%\n")

# Main code
if __name__ == "__main__":
    # Initialize user data
    username_password = {}
    if os.path.exists("user_overview.txt"):
        with open("user_overview.txt", 'r') as user_file:
            user_data = user_file.read().split("\n")
        for user in user_data:
            if user:
                user_components = user.split(';')
                if len(user_components) >= 2:
                    username, password = user_components
                    username_password[username] = password
                else:
                    print(f"Invalid user data: {user}")
                    
    # Initialize task data
    task_list = []
    if os.path.exists("task_overview.txt"):
        with open("task_overview.txt", 'r') as task_file:
            task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]
        for t_str in task_data:
            curr_t = {}
            task_components = t_str.split(";")
            if len(task_components) >= 6:
                curr_t['username'] = task_components[0]
                curr_t['title'] = task_components[1]
                curr_t['description'] = task_components[2]
                curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
                curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
                curr_t['completed'] = True if task_components[5] == "Yes" else False
                task_list.append(curr_t)
            else:
                print(f"Invalid task data: {t_str}")

    # User login
    logged_in = False
    while not logged_in:
        print("=" * 40)
        print("LOGIN")
        curr_user = input("Username: ")
        curr_pass = input("Password: ")
        if curr_user not in username_password.keys():
            print("User does not exist")
            continue
        elif username_password[curr_user] != curr_pass:
            print("Wrong password")
            continue
        else:
            print("Login Successful!")
            logged_in = True

    # Main menu loop
    while True:
        print("=" * 40)
        menu = input('''Please select one of the following options:
        r - Register user
        a - Add task
        va - View all tasks
        vm - View my tasks
        gr - Generate reports
        ds - Display statistics
        e - Exit
        : ''').lower()

        if menu == 'r':
            reg_user(username_password)

        elif menu == 'a':
            add_task(task_list, username_password)

        elif menu == 'va':
            view_all(task_list)

        elif menu == 'vm':
            view_mine(task_list, curr_user)

        elif menu == 'gr':
            generate_reports(task_list, username_password)
            print("Reports generated successfully.")

        elif menu == 'ds' and curr_user == 'admin':
            num_users = len(username_password)
            num_tasks = len(task_list)

            print("=" * 40)
            print(f"Number of users: \t\t {num_users}")
            print(f"Number of tasks: \t\t {num_tasks}")
            print("=" * 40)

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice. Please try again.")

