class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def get_grade(self):
        if self.mark >= 90:
            return "A"
        elif self.mark >= 75:
            return "B"
        elif self.mark >= 60:
            return "C"
        else:
            return "F"
students=[]
while True:
    print("\n1. Add student 2.View all 3.Exit")
    choice=input("Choose: ")
    if choice=="1":
        name=input("Enter name: ")
        mark=float(input("Enter mark: "))
        new_student = Student(name, mark)
        students.append(new_student)
        print(f"Added {name}!")
    elif choice=="2":
        for student in students:
            print(f"Name: {student.name}, Mark: {student.mark}, Grade: {student.get_grade()}")
    elif choice=="3":
        break
    elif choice == "4":
        with open("students.txt", "w") as f:
            for student in students:
                f.write(f"{student.name},{student.mark}\n")
        print("Saved!")
