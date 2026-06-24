# 📖 Personal Journal Manager

## 🌟 Project Overview

**Personal Journal Manager** is a Python-based command-line application that helps users maintain a digital journal. Users can add daily entries, view all saved entries, search for specific entries, and delete all entries when required.

The program stores journal entries in a text file (`journal.txt`) along with the current date and time, making it easy to track thoughts and activities.

---

# 🎯 Objectives

✅ Learn Object-Oriented Programming (OOP)

✅ Understand File Handling in Python

✅ Practice Exception Handling

✅ Work with Date and Time Functions

✅ Build a Real-World Mini Project

---

# ✨ Features

## 📝 1. Add a New Entry

* Allows users to write journal entries.
* Automatically saves the current date and time.
* Stores entries in `journal.txt`.

## 📚 2. View All Entries

* Displays all saved journal entries.
* Reads data directly from the journal file.

## 🔍 3. Search for an Entry

* Search by keyword.
* Search by date.
* Shows matching journal entries.

## 🗑️ 4. Delete All Entries

* Deletes all saved entries.
* Confirmation message prevents accidental deletion.

## ⚠️ 5. Error Handling

* Handles invalid menu inputs.
* Handles missing files.
* Prevents unexpected program crashes.

---

# 🛠️ Technologies Used

| Technology            | Purpose                        |
| --------------------- | ------------------------------ |
| 🐍 Python             | Programming Language           |
| 📂 File Handling      | Store and Read Journal Entries |
| ⚠️ Exception Handling | Error Management               |
| 🕒 datetime Module    | Timestamp Generation           |
| 📁 os Module          | File Deletion                  |

---

# 📂 Project Structure

```text
PersonalJournalManager/
│
├── journal.py
├── journal.txt
└── README.md
```

---

# ▶️ How to Run

### Step 1️⃣ Open Terminal / CMD

```bash
cd PersonalJournalManager
```

### Step 2️⃣ Run the Program

```bash
python journal.py
```

---

# 📋 Menu

```text
1. Add a New Entry
2. View all Entries
3. Search for an Entry
4. Delete all Entries
5. Exit
```

---

# 🖥️ Sample Output Screenshots

## 📌 Program Start

```text
Welcome to Personal Journal Manager!
Please select an option.

1. Add a New Entry
2. View all Entries
3. Search for an Entry
4. Delete all Entries
5. Exit

user Input:
```

---

## 📝 Adding an Entry

```text
user Input: 1

Enter your journal entry:
Today I learned Python File Handling.

Entry added successfully.
```

---

## 📚 Viewing Entries

```text
user Input: 2

Your Journal Entries:
-------------------------------------

[2026-06-19 10:30:15] Today I learned Python File Handling.
[2026-06-19 10:35:20] Completed my Journal Manager project.
```

---

## 🔍 Searching an Entry

```text
user Input: 3

Enter keyword or date to search:
Python

[2026-06-19 10:30:15] Today I learned Python File Handling.
```

---

## 🗑️ Deleting Entries

```text
user Input: 4

Are you sure you want to delete all entries? (yes/no):
yes

All journal entries have been deleted.
```

---

# 🧠 Concepts Used

### 🔹 Classes & Objects

Used to create the `journalmanager` class.

### 🔹 Constructor (`__init__`)

Initializes the journal file name.

### 🔹 File Handling

* Open File
* Read File
* Write File
* Append File

### 🔹 Exception Handling

* FileNotFoundError
* ValueError
* Generic Exceptions

### 🔹 Date & Time

Uses `datetime.now()` for timestamps.

### 🔹 Loops & Conditions

Used for menu-driven execution.

---

# 🚀 Future Enhancements

✅ Edit Existing Entries

✅ Password Protection

✅ User Login System

✅ Export Journal to PDF

✅ GUI Version using Tkinter

✅ Entry Categories & Tags

✅ Cloud Storage Support

---

# 🎓 Learning Outcomes

After completing this project, students will understand:

📌 Object-Oriented Programming

📌 File Handling

📌 Exception Handling

📌 Menu-Driven Programs

📌 Date and Time Management

📌 Python Project Development

---

# 🏁 Conclusion

The Personal Journal Manager is a simple yet effective Python application that demonstrates important programming concepts such as OOP, file handling, exception handling, and user interaction. It provides a practical way for users to maintain personal journal entries while serving as an excellent learning project for Python beginners.

⭐ Easy to Use

⭐ Strong OOP and File Handling Practice

---

## 👨‍💻 Author

**Simran Gohel**

📚 Python Mini Project

🎓 MCA / Computer Science Student

🚀 Learning Python Through Real-World Projects
