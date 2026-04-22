print("\n==== PART 1: Student List ====")
students = ["Esmeralda", "Natan", "Nolan", "Zhask", "Luo Yi"]
students.append("Nana")
students.remove("Luo Yi")
print("Final Student List:", students)

print("\n==== PART 2: Subjects ====")
subjects = ["Math", "Science", "English", "Filipino", "Calculus", "Chemistry"]
print("Total Number of Subjects:", len(subjects))
print("First Subject:", subjects[0])
print("Last Subject:", subjects[-1])
print("Subjects Offered:")
for sub in subjects:
    print("-", sub)

print("\n==== PART 3: Student Grades ====")
grades = {"Esmeralda": 88,"Natan": 72,"Nolan": 95,"Zhask": 65}
grades["Nana"] = 100
grades["Natan"] = 76
grades["Esmeraldo Jr"] = 90   
grades["Zhask"] = 70   
print("Student Grades:")
for name in grades:
    print(name, "=", grades[name])
total = 0
count = 0
for name in grades:
    total = total + grades[name]
    count = count + 1
average = total / count
print("Class Average Grade:", f"{average:.2f}")

print("\n==== PART 4: Passed/Failed Sets ====")
grades = {"Esmeralda": 88,"Natan": 76,"Nolan": 95,"Zhask": 70,"Nana": 100,"Esmeraldo Jr": 90}
passed_students = set()
for name in grades:
    if grades[name] >= 75:
        passed_students.add(name)
failed_students = set()
for name in grades:
    if grades[name] < 75:
        failed_students.add(name)
print("Passed Students:", passed_students)
print("Failed Students:", failed_students)
print("Passed but NOT Failed:", passed_students - failed_students)



