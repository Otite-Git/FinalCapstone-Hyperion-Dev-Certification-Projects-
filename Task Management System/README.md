# 🎒Python Language Projects 🌟
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
**Login**: Enter your username and password to log in. The default Username is: admin. The default password is: password as seen in the screenshot below.

<img width="1139" alt="Screenshot 2024-03-11 at 16 03 14" src="https://github.com/Otite-Git/FinalCapstone-Hyperion-Dev-Certification-Projects-/assets/154989610/12e1dac2-53b4-4df6-916f-d98331150499">




**Main Menu Options**:

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
![Alt text](<Screenshot 2024-03-11 at 16.07.47.png>)
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

# Task Management System User Guide

## Installation with Visual Studio Code

### Prerequisites

Before getting started, ensure you have the following installed on your machine:

1. **Python:** Download and install Python from [Python's official website](https://www.python.org/downloads/).

2. **Visual Studio Code:** If not already installed, download and install Visual Studio Code from [Visual Studio Code's official website](https://code.visualstudio.com/).

### Step 1: Clone the Repository

Open Visual Studio Code, open a terminal, and run the following commands:

```bash
# Clone the repository
git clone https://github.com/your-username/your-repository.git

# Navigate to the project directory
cd your-repository
```
### Step 2: Set Up Virtual Environment

Create and activate a virtual environment to manage dependencies:

```bash
# Create a virtual environment (Windows)
python -m venv venv

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Create a virtual environment (Mac/Linux)
python3 -m venv venv

# Activate the virtual environment (Mac/Linux)
source venv/bin/activate
```

### Step 3: Install Dependencies
Install the required dependencies for the Task Management System:

```bash
pip install -r requirements.txt
```
### Step 4: Run the Program
Start the Task Management System program:

```bash
python Task_Management_System.py
```

Follow the on-screen prompts to log in and use the program.

### Step 5: User and Task Data Files
The program uses two text files (user_overview.txt and task_overview.txt) to store user and task data. Ensure these files are present in the project directory. If they don't exist, the program will create them during execution.

### Step 6: Exiting the Program
To exit the program, select the 'e' option from the main menu.

Feel free to explore and customize the program based on your requirements




