import random
import pandas

names = ["Madhu","Charan","Ram Charan","Deva","Manogna","Laddo"]

student_marks_list = {
    "Name" : names,
    "Marks" : [random.randint(40,100) for _ in range(6)]
}

dataframe = pandas.DataFrame(student_marks_list)
for (index,row) in dataframe.iterrows():
    print(row.Marks)
