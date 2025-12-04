import pandas
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#
# import pandas as pd
# data = pd.read_csv("weather_data.csv")
# print(data["temp"])
# temp_list = data["temp"].to_list()
# print(temp_list)
# max_temp = data["temp"].max() # maximum of temperature
# print(max_temp)
#
# #in order not to have correct spelling use attributes
# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == max_temp]) # methods to print a specified row!
#
#
# monday = data[data["day"] == "Monday"]
# monday_temperature = monday.temp[0]
# monday_temperature = monday_temperature * 9 / 5 + 32
# print(monday_temperature)

data_dict = {
    "students": ["Amy","James","Angela"],
    "scores" : [76,56,65]
}

data_dictionary = pandas.DataFrame(data_dict)
print(data_dictionary)
data_dictionary.to_csv("new_data.csv")
