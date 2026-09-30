# Student Data Organizer

A simple Python program for managing student information through an interactive menu.

This project is mainly focused on practicing Python data structures and basic programming concepts by creating a small student management system.

## Features

- Add new students
- Display all stored students
- Update student information
- Delete a student
- Display subjects offered to a particular student
- Automatically assign student IDs
- Store student information using different Python data structures
- Interactive menu-based interface

## How It Works

When the program starts, it displays a menu with six options:

1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit

### 1. Add Student

The program asks the user to enter the student's:

- Name
- Age
- Grade
- Date of Birth
- Subjects

A student ID is generated automatically, and the complete student record is stored in a dictionary.

The dictionary is then added to the main `students` list.

### 2. Display All Students

This option displays the information of all students currently stored in the program.

The displayed information includes:

- Student ID
- Name
- Age
- Grade
- Subjects

### 3. Update Student Information

The user can enter a student ID and choose which information they want to update.

The available options are:

- ID
- Name
- Age
- Grade
- D.O.B.
- Subjects

The program does not allow the ID or D.O.B. to be directly updated through this menu because they are stored in a tuple-based structure.

### 4. Delete Student

The user can enter a student ID to select a student for deletion.

Before removing the student, the program displays the student's information and asks for confirmation.

The user can either:

- Confirm the deletion
- Cancel the operation

### 5. Display Subjects Offered

This option asks for a student ID and displays the subjects stored for that particular student.

### 6. Exit

Selecting option `6` exits the program.

## Python Concepts Used

### Lists

A list is used to store all student records.

The `students` list contains the dictionaries representing individual students.

### Dictionaries

Each student is represented using a dictionary containing different pieces of information such as ID, name, age, grade, date of birth, and subjects.

### Tuples

The date of birth is converted into a tuple after splitting the entered date using `-`.

For example, a date such as `2008-05-10` is separated into its individual date components.

### Sets

Subjects are stored using a set.

This also prevents duplicate subject values from being stored.

For example, if the user enters the same subject more than once, the set keeps only one occurrence.

### While Loops

A `while` loop keeps the main menu running until the user selects the Exit option.

Another `while` loop is used while updating or deleting student information.

### For Loops

A `for` loop is used to go through the stored student records when displaying them.

### Conditional Statements

`if`, `elif`, and `else` statements are used to handle different menu choices and user actions.

### Type Conversion

The `int()` function is used to convert values such as age and menu choices from strings into integers.

### String Formatting

The program uses multiple Python string formatting techniques, including f-strings, `.format()`, and `%` formatting.

## Data Structures Used

| Data Structure | Purpose |
|---|---|
| List | Stores all student records |
| Dictionary | Stores information of an individual student |
| Tuple | Stores date of birth components |
| Set | Stores subjects |

## Example

A typical interaction with the program looks like this:

    Welcome to the Student Data Organizer!

    Select an option:
    1. Add Student
    2. Display All Students
    3. Update Student Information
    4. Delete Student
    5. Display Subjects Offered
    6. Exit

    Enter your choice: 1

    Enter student details:
    Student ID: 101
    Name: Uvesh
    Age: 18
    Grade: A
    Date of Birth (YYYY-MM-DD): 2008-05-10
    Subjects (comma-separated): Python,Math,English

    Student added successfully!

## Requirements

You only need Python installed on your computer.

To check your Python installation, run:

    python --version

## How to Run

1. Download or clone this repository.
2. Open the project folder in a terminal.
3. Run the Python file using:

       python main.py

4. Select an option from the menu.
5. Follow the instructions shown by the program.

## Purpose

This project was created as a practical exercise for understanding how different Python data structures can work together in a single program.

It combines lists, dictionaries, tuples, and sets with loops, conditional statements, user input, and basic CRUD-style operations such as adding, displaying, updating, and deleting student records.

---

Made for learning Python through practice. 🐍
