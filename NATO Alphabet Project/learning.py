import random

numbers = [1,2,3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Madhu"
newList = [letter for letter in name]
print(newList)

names = ["Madhu","Charan","Ram Charan","Deva","Manogna","Laddo"]
new_List = [name for name in names if "M" in name]
print(new_List)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)


student_names = {student: random.randint(1,100) for student in names}
print(student_names)

passed_students = {student: score for (student,score) in student_names.items() if score >= 60}
print(passed_students)