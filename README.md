
**🎓 Student Management System**
A simple, menu-driven Python app for keeping student records in order. Add a student, look them up by ID, update their marks, or see how the class is doing—all from the command line.
✨ What it can do
- Add students with an ID, name, age, standard, and marks
- Display all students in the current session
- Search for a student by ID
- Update a student’s marks, with a 0–100 range check
- Delete a student record by ID
- Calculate the average marks of the students currently in memory
- Save and load records using students.csv
🧱 How it’s organized
- Person is an abstract base class holding the common name and age fields.
- Student inherits from Person and adds student-specific details and mark accessors.
- Student_Management handles the menu, student list, and CSV operations.
🚀 Getting started
Save the code in a Python file, such as student_management.py, then run:
python student_management.py
Choose an option from the menu and follow the prompts.
💾 Saving and loading records
Select 7 to save the current student list to students.csv. Select 8 to load records from that file. The CSV file is created in the directory where the program is run.
🗂️ CSV format
The saved file uses these columns:
Student_ID,Name,Age,Standard,Marks
🧭 A quick tour
--- Student Management System ---
1. Add Student
2. Display Students
3. Search Student
4. Update Student
5. Delete Student
6. Calculate Average Marks
7. Save Records
8. Load Records
9. Exit
🔎 A couple of things to keep in mind
- Student records are kept in memory while the program runs; save them before exiting if you want to keep them.
- Loading records appends them to the current list. Loading the same file more than once may create duplicate entries.
- Marks entered when adding a student are not range-checked; the 0–100 check applies when updating marks.
- Some menu actions expect numeric input, so entering text where an ID or mark is requested may raise an error.
🌱 Possible next steps
Add duplicate-ID checks, validate all input consistently, and support editing a student’s name or standard.
