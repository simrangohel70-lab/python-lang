print("Welcome to the Pattern Generator and Number Analyzer!")

while True:

    print("\nMenu")
    print("1. Generate a Pattern")
    print("2. Analyze Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        rows = int(input("Enter number of rows: "))

        if rows <= 0:
            print("Please enter a positive number!")
        else:
            print("\nPattern:")

            for i in range(1, rows + 1):
                for j in range(i):
                    print("*", end="")
                print()

    elif choice == 2:

        start = int(input("Enter start number: "))
        end = int(input("Enter end number: "))

        if end < start:
            print("End number must be greater than start number!")
        else:

            total = 0

            for i in range(start, end + 1):

                if i % 2 == 0:
                    print(i, "is Even")
                else:
                    print(i, "is Odd")

                total = total + i

            print("Sum of numbers =", total)

    elif choice == 3:
        print("Thank you for using the program!")
        break

    else:
        print("Invalid choice! Please try again.")