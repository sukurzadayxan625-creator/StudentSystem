from database import loadStudents, saveStudents


def addStudent(name, age, course):
    students = loadStudents()

    studentId = 1
    for student in students:
        if student["id"] >= studentId:
            studentId = student["id"] + 1

    newStudent = {
        "id": studentId,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(newStudent)
    saveStudents(students)
    return newStudent


def showStudents():
    return loadStudents()


def updateStudent(studentId, name, age, course):
    students = loadStudents()

    for student in students:
        if student["id"] == studentId:
            student["name"] = name
            student["age"] = age
            student["course"] = course
            saveStudents(students)
            return True

    return False


def deleteStudent(studentId):
    students = loadStudents()
    newStudents = []
    foundStudent = False

    for student in students:
        if student["id"] == studentId:
            foundStudent = True
        else:
            newStudents.append(student)

    if foundStudent:
        saveStudents(newStudents)

    return foundStudent


def searchStudents(searchText):
    students = loadStudents()
    foundStudents = []
    searchText = searchText.lower()

    for student in students:
        if (searchText in student["name"].lower()
                or searchText in student["course"].lower()
                or searchText == str(student["id"])):
            foundStudents.append(student)

    return foundStudents
