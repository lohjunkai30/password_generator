import random
import string

# Logic of the password_generator is to autogenerate the special requirements first such as numbers, special characters and Uppercase followed by adding the required lowercase and then finally reshuffling the string for a final password.


def generate_password(list1):
    length, num_upper, num_num, num_special = list1
    list_of_lower = string.ascii_lowercase
    list_of_upper = string.ascii_uppercase
    list_of_numbers = string.digits
    list_of_special = ["@", "!", "-", "_", "?"]
    password = ""

    # Autogenerating the special requirements
    while num_upper != 0:
        password += random.choice(list_of_upper)
        length -= 1
        num_upper -= 1
    while num_num != 0:
        password += random.choice(list_of_numbers)
        length -= 1
        num_num -= 1
    while num_special != 0:
        password += random.choice(list_of_special)
        length -= 1
        num_special -= 1

    # Adding the required lowercase characters to meet the length requirement
    remaining_lower = ''.join(random.choice(list_of_lower) for i in range(length))
    password += remaining_lower

    # Reshuffling the string for a random sequence
    shuffled_password = random.sample(password, k=len(password))
    return "".join(shuffled_password)


