students = {}

# Function to add student
def add_student():
    student_id = int(input("Enter Student ID: "))      
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    grade = input("Enter Grade: ")

    subjects = set(input("Enter subjects (comma separated): ").split(","))

    dob = input("Enter Date of Birth (DD-MM-YYYY): ")
    unique_info = (student_id, dob)   

    students[student_id] = {
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects,
        "unique_info": unique_info
    }

    print(f"\nStudent Added: {name}, Age: {age}, Grade: {grade}")  
    print("Student {} is in grade {}".format(name, grade))        
    print("Name: %s | Age: %d" % (name, age))                     


# display all students
def display_students():
    print("\n===== Student List =====")
    if not students:
        print("No students found!")
    else:
        for sid, details in students.items():
            print(f"ID: {sid}, Name: {details['name']}, Age: {details['age']}, Grade: {details['grade']}, Subjects: {', '.join(details['subjects'])}")


# Function to modify (List mutability example)
def modify_student():
    sid = int(input("Enter Student ID to modify: "))
    if sid in students:
        new_name = input("Enter new name: ")
        students[sid]["name"] = new_name
        print("Name updated successfully!")
    else:
        print("Student not found!")


# Function to delete a student
def delete_student():
    sid = int(input("Enter Student ID to delete: "))
    if sid in students:
        del students[sid]  
        print("Student deleted successfully!")
    else:
        print("Student not found!")


# Main Menu Loop
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Modify Student Name")
    print("4. Delete Student")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:   
        modify_student()
    elif choice == 4:       
        delete_student()
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")