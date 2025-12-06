# Keyword Method with to_dict() - more efficient than iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = data.set_index('letter')['code'].to_dict()
print(phonetic_dict)

while True:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError as error:
        print(f"There is no alphabet {error} in dictionary\nPlease try again")
    else:
        print(output_list)
        break
