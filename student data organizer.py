students = []

while True:

    print("\n----- Student Data Organizer -----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    # Add Student
    if choice == 1:

        sid = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        grade = input("Enter Grade: ")

        dob = input("Enter DOB (YYYY-MM-DD): ")
        dob = tuple(dob.split("-"))

        subjects = set(input("Enter Subjects (comma separated): ").split(","))

        student = {
            "id": sid,
            "name": name,
            "age": age,
            "grade": grade,
            "dob": dob,
            "subjects": subjects
        }

        students.append(student)

        print("Student Added Successfully!")

    # Display Students
    elif choice == 2:

        for s in students:
            print("\nID:", s["id"])
            print("Name:", s["name"])
            print("Age:", s["age"])
            print("Grade:", s["grade"])
            print("DOB:", "-".join(s["dob"]))
            print("Subjects:", ", ".join(s["subjects"]))

    # Update Student
    elif choice == 3:

        sid = int(input("Enter Student ID: "))

        for s in students:
            if s["id"] == sid:

                s["age"] = int(input("Enter New Age: "))
                s["grade"] = input("Enter New Grade: ")

                print("Student Updated!")
                break

    # Delete Student
    elif choice == 4:

        sid = int(input("Enter Student ID: "))

        for i in range(len(students)):
            if students[i]["id"] == sid:
                del students[i]
                print("Student Deleted!")
                break

    # Display Subjects
    elif choice == 5:

        all_subjects = set()

        for s in students:
            all_subjects.update(s["subjects"])

        print("\nSubjects Offered:")
        for subject in all_subjects:
            print(subject)

    # Exit
    elif choice == 6:
        print("Thank You For Using Student Data Organizer!")
        break

    else:
        print("Invalid Choice!")