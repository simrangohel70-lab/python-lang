data = []


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def dataset_statistics(arr):
    minimum = min(arr)
    maximum = max(arr)
    total = sum(arr)
    average = total / len(arr)
    return minimum, maximum, total, average

while True:
    print("\nWelcome to the Data Analyzer and Transformer Program")
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = int(input("Please enter your choice: "))

    if choice == 1:
        print("\nStep 1: Input Data")
        data = list(map(int, input(
            "Enter data for a 1D array (separated by spaces): ").split()))
        print("Data has been stored successfully!")

    elif choice == 2:
        print("\nStep 2: Display Data Summary")
        if data:
            print("\nData Summary:")
            print("- Total elements:", len(data))
            print("- Minimum value:", min(data))
            print("- Maximum value:", max(data))
            print("- Sum of all values:", sum(data))
        else:
            print("No data available!")

    elif choice == 3:
        print("\nStep 3: Calculate Factorial (Recursion)")
        num = int(input("Enter a number to calculate its factorial: "))
        print(f"Factorial of {num} is: {factorial(num)}")

    elif choice == 4:
        print("\nStep 4: Filter Data by Threshold (Lambda Function)")
        if data:
            threshold = int(
                input("Enter a threshold value to filter out data above this value: "))
            filtered = list(filter(lambda x: x >= threshold, data))
            print(f"\nFiltered Data (values >= {threshold}):")
            print(*filtered, sep=", ")
        else:
            print("No data available!")

    elif choice == 5:
        print("\nStep 5: Sort Data")
        if data:
            print("1. Ascending")
            print("2. Descending")
            order = int(input("Enter your choice: "))

            if order == 1:
                sorted_data = sorted(data)
                print("\nSorted Data in Ascending Order:")
                print(*sorted_data, sep=", ")

            elif order == 2:
                sorted_data = sorted(data, reverse=True)
                print("\nSorted Data in Descending Order:")
                print(*sorted_data, sep=", ")
        else:
            print("No data available!")

    elif choice == 6:
        print("\nStep 6: Display Dataset Statistics")
        if data:
            minimum, maximum, total, average = dataset_statistics(data)

            print("\nDataset Statistics:")
            print("- Minimum value:", minimum)
            print("- Maximum value:", maximum)
            print("- Sum of all values:", total)
            print("- Average value:", round(average, 2))
        else:
            print("No data available!")

    elif choice == 7:
        print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")