try:
    file = open("data.txt")
    dictionary = {"Key": "Value"}
    value = dictionary["Another_key"]
except FileNotFoundError:
    print("File not found")
except KeyError as error:
    print(f"There is no such {error} in dictionary")
else:
    data_file = file.read()
    print(data_file)
    print(value)
    file.close()