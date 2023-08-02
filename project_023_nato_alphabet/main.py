import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

name = input("Enter your name : ").upper()
output_list = [nato_dict[word] for word in name]
print(output_list)