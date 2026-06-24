import os
from datetime import datetime


class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"

    def add_entry(self):
        entry = input("Enter your journal entry: ")

        with open(self.filename, "a") as file:
            file.write(f"\n[{datetime.now()}]\n{entry}\n")

        print("Entry added successfully!")

    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                print("\nJournal Entries:\n")
                print(file.read())

        except FileNotFoundError:
            print("No journal entries found!")

    def search_entry(self):
        try:
            keyword = input("Enter keyword to search: ")

            with open(self.filename, "r") as file:
                data = file.read()

            if keyword.lower() in data.lower():
                print("\nMatch Found:\n")
                print(data)
            else:
                print("No matching entry found!")

        except FileNotFoundError:
            print("Journal file does not exist!")

    def delete_entries(self):
        if os.path.exists(self.filename):
            choice = input("Delete all entries? (yes/no): ")

            if choice.lower() == "yes":
                os.remove(self.filename)
                print("All entries deleted!")
        else:
            print("No journal entries to delete!")


journal = JournalManager()

while True:
    print("\n===== Personal Journal Manager =====")
    print("1. Add New Entry")
    print("2. View All Entries")
    print("3. Search Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        journal.add_entry()

    elif choice == "2":
        journal.view_entries()

    elif choice == "3":
        journal.search_entry()

    elif choice == "4":
        journal.delete_entries()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")