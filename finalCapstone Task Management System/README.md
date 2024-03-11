# 🎒HyerionDev Bootcamp Projects & Personal Projects 🌟
Hi! Welcome to my Task Management Sysmtem Folder containg the Python Project 🚀:

In this repository you will see a description of the Task Management System project that I have developed as part of my personal progressive development of my code skills.

## Task Management System

## Overview
This Python program serves as a task management system allowing users to register, add tasks, and generate reports. Users can register with a unique username and password, add tasks with specific details, and view tasks based on different criteria. The program also offers administrative functions like generating reports and displaying statistics.

## Features
### User Registration
**Register New User**: Users can register by providing a unique username and password. The system checks for existing usernames to ensure uniqueness.

## Task Management
**Add Task**: Users can add tasks by specifying the assigned username, task title, description, due date, and other details. Task data is stored in the "tasks.txt" file.
**View All Tasks**: Users can view all tasks in a detailed format, including assigned user, due date, and task description.
**View User-Specific Tasks**: Users can view tasks assigned to them, with options to mark tasks as complete or edit task details.

## Reporting
**Generate Reports**: The system can generate task overview and user overview reports, providing insights into the total tasks, completed tasks, overdue tasks, and user-specific statistics. Reports are stored in separate text files ("task_overview.txt" and "user_overview.txt").
Statistics (Admin Only)
**Display Statistics**: Admin users can display basic statistics such as the number of users and tasks.

## File Management
### User Data
User data is stored in the "user.txt" file, where each line represents a user with the format: username;password.

### Task Data
Task data is stored in the "tasks.txt" file, where each line represents a task with the format: username;title;description;due_date;assigned_date;completed.

### Generated Reports
Task overview and user overview reports are stored in "task_overview.txt" and "user_overview.txt," respectively.

### How to Use
**Login**: Enter your username and password to log in.

***Main Menu Options**:

**r**: Register a new user.
**a**: Add a new task.
**va**: View all tasks.
**vm**: View tasks assigned to you and perform actions like marking as complete or editing.
**gr**: Generate reports.
**ds**: Display statistics (admin only).
**e**: Exit the program.

### Register New User:

Choose **'r'** from the main menu.
Enter a new username and password.
Add Task:

Choose **'a'** from the main menu.
Provide details such as the assigned user, task title, description, and due date.
View Tasks:

Choose **'va'** to view all tasks.
Choose **'vm'** to view tasks assigned to you.

**Generate Reports**:

Choose **'gr'** to generate reports, providing an overview of tasks and user statistics.
Display Statistics (Admin Only):

Choose **'ds'** to display basic statistics (admin only).
**Exit:**

Choose **'e'** to exit the program.

## Caution
The program relies on accurate date and time formatting. Use the specified "YYYY-MM-DD" format for due dates.
Admin functions are powerful and should be used responsibly.
Ensure the proper closing of the program using the 'e' (exit) option to avoid data loss or corruption.
Feel free to manage your tasks efficiently using this system, and thank you for using our task management program!

## Note
Ensure data integrity by following the specified formats for usernames, passwords, and datetime entries.
Admin functionalities (display statistics) are only available to users with the username 'admin.'
Feel free to manage your tasks efficiently using this system, and thank you for using our task management program!

# Task Management System

## Installation

Follow these steps to install and run the Task Management System Python program on your local machine:

### Prerequisites

- Ensure you have Python installed on your machine. If not, you can download it from [Python's official website](https://www.python.org/downloads/).

### Clone the Repository

**```bash**
git clone https://github.com/your-username/your-repository.git
cd your-repository
Run the Program
Open a terminal or command prompt and navigate to the project directory. Run the following command to execute the program:

**bash**
***Copy code***
python Task_Management_System.py
User and Task Data Files
The program uses two text files (user_overview.txt and task_overview.txt) to store user and task data. Make sure these files are present in the project directory. If they don't exist, the program will create them during execution.

**Login**
Follow the on-screen prompts to log in with your username and password. If you're a new user, you'll be prompted to register before logging in.

**Main Menu**
Once logged in, you'll be presented with a main menu where you can perform various actions, such as registering a new user, adding tasks, viewing tasks, generating reports, and more.

**Exit**
To exit the program, select the 'e' option from the main menu.

Feel free to explore and customize the program based on your requirements!

javascript
Copy code

Replace `your-username` and `your-repository` with your actual GitHub username and repository name. This section provides users with clear instructions on how to install and run your Task Management System Python program locally.




