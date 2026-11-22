import json 
import os


dataFile = os.path.join(os.path.dirname(__file__), "students.json")


def loadStudents():
    try:
        file = open(dataFile, "r", encoding="utf-8")
        students = json.load(file)
        file.close()
        return students
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("JSON faylında xəta var.")
        return []


def saveStudents(students):
    file = open(dataFile, "w", encoding="utf-8")
    json.dump(students, file, ensure_ascii=False, indent=4)
    file.close()
