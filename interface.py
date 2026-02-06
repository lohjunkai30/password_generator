import string
from collections import defaultdict
from password_generator import generate_password

# Utilising a dcitionary to obtain required input through f strings and store input neatly
dict_of_answers = {
    "Length of Password": 0,
    "Number of Uppercase": 0,
    "Number of Numbers": 0,
    "Number of Special Characters": 0
}

# Rough Python Interface
print("Hello! Do answer the following questions to receive your generated password. Remember to only answer with numbers")
for i in dict_of_answers:
    # Ensures that only numbers are inputted. Rejects strings
    try:
        int1 = int(input(f"Hello! Please input {i}"))
        dict_of_answers[i] = int1
    except Exception as e:
        print(f"Sorry. Your input was not processed due to {e}")

# Logic Check to ensure that length of password is the largest number 
list_of_values = list(dict_of_answers.values())
if (list_of_values[0] < sum(list_of_values[1:])):
    print("Error Found! Length of Password is too small")

print("Generating Password...")

# Generation of desired password
print(generate_password(list_of_values))



