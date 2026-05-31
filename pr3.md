# Student Management System

## Overview

Student Management System is a simple Python console-based application that allows users to manage student records. The project demonstrates the use of Python data structures such as dictionaries, sets, tuples, and functions.

## Features

* Add new student records
* Display all students
* Modify student names
* Delete student records
* Store student subjects using sets
* Store unique student information using tuples
* User-friendly menu-driven interface

## Technologies Used

* Python 3
* Dictionary
* Set
* Tuple
* Functions
* Loops and Conditional Statements

## Data Structure Used

### Dictionary

Stores all student records with Student ID as the key.

```python
students = {}
```

### Set

Stores subjects without duplicates.

```python
subjects = set(input("Enter subjects (comma separated): ").split(","))
```

### Tuple

Stores unique information such as Student ID and Date of Birth.

```python
unique_info = (student_id, dob)
```

## Menu Options

### 1. Add Student

Allows the user to enter:

* Student ID
* Name
* Age
* Grade
* Subjects
* Date of Birth

### 2. Display All Students

Shows details of all stored students.

### 3. Modify Student Name

Updates the name of an existing student using their Student ID.

### 4. Delete Student

Removes a student record from the system.

### 5. Exit

Closes the application.

## How to Run

1. Install Python 3.
2. Save the code in a file named:

```bash
student_management.py
```

3. Open terminal or command prompt.
4. Run the program:

```bash
python student_management.py
```

## Example Output

```text
===== Student Management System =====
1. Add Student
2. Display All Students
3. Modify Student Name
4. Delete Student
5. Exit

Enter your choice: 1

Enter Student ID: 101
Enter Student Name: Rahul
Enter Student Age: 18
Enter Grade: A
Enter subjects (comma separated): Math,Science,English
Enter Date of Birth (DD-MM-YYYY): 10-05-2006

Student Added: Rahul, Age: 18, Grade: A
```

## Learning Concepts Covered

* Functions
* Dictionaries
* Sets
* Tuples
* String Formatting

  * f-strings
  * format()
  * % formatting
* Loops
* Conditional Statements
* CRUD Operations

## Author

Developed as a Python Mini Project for learning basic programming concepts and data structures.
