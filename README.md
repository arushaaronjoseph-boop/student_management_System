# 🎓 Student Management System

> **A small command-line classroom for student records:** add a learner, look up their details, update marks, and keep a CSV copy for later. 📚

This project is a beginner-friendly Python program for managing student information in a terminal. It brings together object-oriented programming concepts—abstract classes, inheritance, encapsulation, and methods—with everyday record operations such as searching, calculating averages, and saving data.

The system keeps its records in memory while it runs. When you choose **Save Records**, it writes those records to `students.csv`; **Load Records** reads that file back into the current session.

---

## 📑 Contents

- [✨ What it can do](#-what-it-can-do)
- [🧭 A quick tour](#-a-quick-tour)
- [🏗️ How the code is organized](#️-how-the-code-is-organized)
- [🧰 Requirements](#-requirements)
- [🚀 Getting started](#-getting-started)
- [🖥️ Using the menu](#️-using-the-menu)
- [📄 CSV file format](#-csv-file-format)
- [🧠 Object-oriented concepts in the project](#-object-oriented-concepts-in-the-project)
- [🔎 Current behavior and practical notes](#-current-behavior-and-practical-notes)
- [🌱 Ideas for future improvements](#-ideas-for-future-improvements)
- [✅ Learning checklist](#-learning-checklist)

---

## ✨ What it can do

| Menu option | What happens |
| --- | --- |
| ➕ Add Student | Prompts for a student ID, name, age, standard, and marks |
| 📋 Display Students | Prints every student currently held in memory |
| 🔍 Search Student | Finds a student by ID and displays their information |
| ✏️ Update Student | Changes the marks for the matching student ID |
| 🗑️ Delete Student | Removes the matching student from the current session |
| 📊 Calculate Average Marks | Calculates the mean marks for the students currently in memory |
| 💾 Save Records | Writes the in-memory records to `students.csv` |
| 📥 Load Records | Appends rows from `students.csv` to the in-memory list |
| 🚪 Exit | Ends the program |

---

## 🧭 A quick tour

A typical session might look like this:

1. ➕ Start the program and choose **1** to add a student.
2. 📝 Enter the requested details. IDs and ages should be whole numbers; marks should be numeric.
3. 📋 Choose **2** to see the records you have entered.
4. 📊 Choose **6** to calculate the average marks.
5. 💾 Choose **7** to save the current records in `students.csv`.
6. 📥 On a later run, choose **8** to load the saved records.

The menu repeats until you select **9**. The CSV file is stored relative to the program's **current working directory**—the directory from which Python was launched.

---

## 🏗️ How the code is organized

The program has three main classes:

- **`Person`** describes the information shared by people: a name and age. It is an abstract base class, so it also requires subclasses to provide a `display_info()` method.
- **`Student`** extends `Person` with a student ID, standard, and marks. It implements `display_info()` and provides accessors for student ID, standard, and marks.
- **`Student_Management`** owns the list of students and implements the menu actions, including CSV persistence.

At the bottom of the file, the program creates a `Student_Management` instance and immediately starts its menu.

---

## 🧰 Requirements

- 🐍 Python 3
- 📦 No third-party packages

The program uses Python's built-in `abc` and `csv` modules.

---

## 🚀 Getting started

1. Save the supplied code in a Python file, for example `student_management.py`.
2. Open a terminal in the folder containing that file.
3. Run:

   ```bash
   python student_management.py
   ```

   On some systems, the command may be:

   ```bash
   python3 student_management.py
   ```

The program starts interactively as soon as the file is run. Follow the prompts and type a menu number. 🎉

---

## 🖥️ Using the menu

### ➕ Add a student

Choose **1** and enter each requested field. The program converts ID and age to integers and marks to a floating-point number. If one of those conversions fails, it prints a validation message and does not add that record.

Example input:

```text
Enter the ID: 1001
Enter the Name: Asha Patel
Enter the age: 15
Enter the Standard: 10
Enter the Marks: 87.5
```

### 📋 Display all students

Choose **2** to print the records currently in memory. If the list is empty, the program reports that no students are available.

### 🔍 Search by student ID

Choose **3**, then enter the ID to look up. The first matching student is displayed. If no record has that ID, the program prints **Student not found.**

### ✏️ Update marks

Choose **4**, provide a student ID, and enter the new marks. The `Student.set_marks()` method accepts values from 0 through 100, inclusive. An out-of-range value produces a message and leaves the marks unchanged.

### 🗑️ Delete a student

Choose **5** and enter the ID. The matching record is removed from memory. To keep this deletion in the CSV file, choose **7** afterward to save the updated list.

### 📊 Calculate the average

Choose **6** to average the marks of all students currently in memory. An empty list has no average, so the program displays a message instead.

### 💾 Save and load

Choose **7** to write the current list to `students.csv`. Choose **8** to read rows from that file into the list. See [CSV file format](#-csv-file-format) for the columns.

---

## 📄 CSV file format

The saved file has a header row followed by one row per student:

```csv
Student_ID,Name,Age,Standard,Marks
1001,Asha Patel,15,10,87.5
```

The file is created in the current working directory. Saving opens it in write mode, so a save replaces the previous contents with the current in-memory list. Loading expects the same headers and numeric formats shown above.

---

## 🧠 Object-oriented concepts in the project

### 🧩 Abstraction

`Person` inherits from `ABC` and declares `display_info()` with `@abstractmethod`. This expresses a shared contract: a concrete kind of person must know how to display its own details. Because `Student` implements the method, it can be instantiated.

### 🧬 Inheritance

`Student(Person)` reuses the base class's name and age setup by calling `super().__init__(name, age)`. Its own constructor adds the student-specific fields.

### 🔐 Encapsulation

Student ID, standard, and marks use double-underscore attribute names such as `__student_id`. The class exposes methods to read those values and to update marks with a range check. Name and age use a single leading underscore to signal that they are intended for internal use.

### 🧱 Separation of responsibilities

The `Student` class represents one record. The management class stores and operates on a collection of records. This keeps student data and menu workflows in distinct places, even though the menu and storage logic currently live in one manager class.

---

## 🔎 Current behavior and practical notes

This README describes what the supplied code does today:

- 🧠 Student records are held in a Python list while the program is running. They are not automatically saved when the program exits.
- 💾 Saving writes the full in-memory list to `students.csv`, replacing any existing file.
- 📥 Loading appends file rows to the existing in-memory list. Loading more than once can therefore create duplicate entries.
- 🆔 The program does not check that student IDs are unique.
- 📏 Adding a student converts marks to a number but does not apply the 0–100 range check. That check runs through `set_marks()` when marks are updated.
- ⚠️ Search, update, and delete convert entered IDs to integers without handling a non-numeric input. Entering text at those prompts can stop the program with a `ValueError`.
- 🧾 Loading handles a missing `students.csv` file, but malformed rows or missing columns are not handled.
- 🎂 The age field is converted to an integer on input, but the code does not enforce an age range.
- ✍️ Names and standards are stored as entered. The program does not validate that they are non-empty.

These are useful next steps for turning the example into a more resilient application.

---

## 🌱 Ideas for future improvements

- 🆔 Validate student IDs for uniqueness before adding a record.
- 📏 Apply the same marks validation during creation and update.
- 🛡️ Handle invalid menu, search, update, and delete input without exiting unexpectedly.
- 📂 Ask before overwriting a CSV file, or add an option to export to a chosen path.
- 🔄 Replace the in-memory list when loading, or detect already-loaded records.
- 🧹 Catch malformed CSV data and explain which row needs attention.
- 🏅 Add sorting, grade bands, class-level summaries, or per-student reports.
- 🧪 Add automated tests for record creation, validation, averages, and CSV round trips.
- 🗂️ Separate the user interface, record operations, and CSV storage into smaller modules as the project grows.

---

## ✅ Learning checklist

After exploring the code, try to answer these questions:

1. ❓ Why can `Person` not be instantiated directly?
2. 🔧 What does `super().__init__(name, age)` accomplish?
3. 🔐 Why does `Student` use getters for some fields?
4. 📄 What happens to the existing CSV contents when records are saved?
5. 🔁 Why can loading the same file twice create duplicate students?
6. 🧭 Where would you add a duplicate-ID check?
7. 🛡️ How could you prevent an invalid search ID from terminating the program?

A good extension exercise is to implement those last two improvements, then test them with both valid and invalid input. 🧪

---

## 📜 License

No license was included with the supplied code. Add a license file if you intend to share or redistribute the project.



