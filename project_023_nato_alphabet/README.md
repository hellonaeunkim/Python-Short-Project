# project_23_nato_alphabet

This code reads data from a CSV file called "nato_phonetic_alphabet.csv" using the Pandas library. The CSV file contains a table with columns "letter" and "code," representing the NATO phonetic alphabet.

Then, the code prompts the user to enter their name, which is stored in the variable "name." The name is converted to uppercase using the upper() method to ensure consistency.

Next, the code creates a list called "output_list," where each element of the list is the NATO phonetic code corresponding to each letter in the user's name. It does this by iterating through each letter in the name and looking up the corresponding code in the previously created "nato_dict" dictionary, which maps each letter to its NATO phonetic code.

Finally, the "output_list" is printed, showing the NATO phonetic code representation of the user's name.






