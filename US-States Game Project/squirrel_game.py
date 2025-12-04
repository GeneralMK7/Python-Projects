import pandas

data_file = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data_file['Primary Fur Color']
count_gray = len(data_file[data_file['Primary Fur Color'] == "Gray"])
count_black = len(data_file[data_file['Primary Fur Color'] == "Black"])
count_Cinnamon = len(data_file[data_file['Primary Fur Color'] == "Cinnamon"])
data_dict = {
    "Fur Color" : ["Gray","Cinnamon","Black"],
    "Count" : [count_gray,count_Cinnamon,count_black]
}

data = pandas.DataFrame(data_dict)
print(data)