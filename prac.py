def save_student(students,filename):
    with open(filename,'w') as f:
        for student in students:
            name=student["name"]
            marks=student["marks"]
            grade=student["grade"]
            f.write(f"name: {name}, marks: {marks}, grade: {grade}\n")
            loaded.append({"name": name,"marks":int(marks),"grade": grade})
        return loaded

#testing
save_student(students,"students.txt")
reloaded=load_students(students.txt)
print(reloaded)