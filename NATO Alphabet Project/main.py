import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = data.set_index('letter')['code'].to_dict()

name = input("Enter the name : ").upper()
nato_alphabet = []
for letter in name:
    nato_alphabet.append(data_dict[letter])
print(nato_alphabet)