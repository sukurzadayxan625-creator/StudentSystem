# Student Management System

This is a simple student management program written in Python. It saves student information in a JSON file.

## Run the program

1. Make sure Python is installed.
2. Open a terminal in this folder.
3. Run this command:

```bash
python main.py
```

## Features

Choose an option from the menu:

1. **Add student** — saves a student's name, age, and course.
2. **Show students** — displays all saved students.
3. **Update student** — changes a student's information using their ID.
4. **Delete student** — removes a student using their ID.
5. **Search student** — searches by name, course, or ID.
0. **Exit** — closes the program.

## Project files

- `main.py` — displays the menu and gets information from the user.
- `students.py` — contains the functions to add, show, update, delete, and search for students.
- `database.py` — reads information from and writes information to the JSON file.
- `students.json` — stores the student information.

The starting content of `students.json` should be:

```json
[]
```

The program adds student information to this file when you use the menu.

## Python topics used

- Functions
- Modules and `import`
- JSON files
- `try/except` for handling errors
- Lists and `for` loops

Function and variable names use camelCase, for example: `addStudent`, `searchStudents`, and `studentId`.
#