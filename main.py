from students import addStudent, showStudents, updateStudent, deleteStudent, searchStudents 


def printStudents(students):
    if len(students) == 0:
        print("Teleb tapilmadi.")
    else:
        for student in students:
            print("ID:", student["id"])
            print("Ad:", student["name"])
            print("Yas:", student["age"])
            print("Kurs:", student["course"])   
            print("--------------------")


def main():
    while True:
        print("\nTelebe Idareetme Sistemi")
        print("1. Telebe elave et")
        print("2. Telebeleri goster")
        print("3. Telebeni yenile")
        print("4. Telebeni sil")
        print("5. Telebe axtar")
        print("0. Cixis")

        choice = input("Seciminizi daxil edin: ")

        try:
            if choice == "1":
                name = input("Telebenin adi: ")
                age = int(input("Telebenin yasi: "))
                course = input("Telebenin kursu: ")
                student = addStudent(name, age, course)
                print("Telebe elave edildi. ID:", student["id"])

            elif choice == "2":
                students = showStudents()
                printStudents(students)

            elif choice == "3":
                studentId = int(input("Yenilenecek telebenin ID-si: "))
                name = input("Yeni ad: ")
                age = int(input("Yeni yas: "))
                course = input("Yeni kurs: ")

                if updateStudent(studentId, name, age, course):
                    print("Telebe yenilendi.")
                else:
                    print("Bu ID ile telebe tapilmadi.")

            elif choice == "4":
                studentId = int(input("Silinecek telebenin ID-si: "))

                if deleteStudent(studentId):
                    print("Telebe silindi.")
                else:
                    print("Bu ID ile telebe tapilmadi.")

            elif choice == "5":
                searchText = input("Ad, kurs ve ya ID daxil edin: ")
                students = searchStudents(searchText)
                printStudents(students)

            elif choice == "0":
                print("Proqram baglandi.")
                break

            else:
                print("Secim duzgun deyil.")

        except ValueError:
            print("Xeta: reqem daxil edin.")
        except OSError:
            print("Xeta: fayli oxumaq ve ya yazmaq mumkun olmadi.")


if __name__ == "__main__":
    main
