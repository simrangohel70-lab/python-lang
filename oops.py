class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("\nPerson Details:")
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        print("\nEmployee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def show_details(self):
        print("\nManager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)
        print("Department:", self.department)


person = None
employee = None
manager = None

while True:
    print("\n--- Python OOP Project: Employee Management System ---")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        person = Person(name, age)
        print("Person created successfully!")

    elif choice == 2:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        employee = Employee(name, age, emp_id, salary)
        print("Employee created successfully!")

    elif choice == 3:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")
        manager = Manager(name, age, emp_id, salary, department)
        print("Manager created successfully!")

    elif choice == 4:
        print("\n1. Person")
        print("2. Employee")
        print("3. Manager")

        option = int(input("Choose detail to show: "))

        if option == 1 and person:
            person.show_details()
        elif option == 2 and employee:
            employee.show_details()
        elif option == 3 and manager:
            manager.show_details()
        else:
            print("Data not available!")

    elif choice == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")