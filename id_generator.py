
import string
import random



def generate_letter():
    first_letter = random.choice(string.ascii_uppercase)
    return first_letter

def generate_first_number():
    first_number = random.randint(1, 2)
    return first_number

def generate_second_to_seventh_number():
    num_list = []
    for i in range(0, 7):
        num = random.randint(0, 9)
        num_list.append(num)
    return num_list


def generate_last_number(id_list):
    letter_dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16,
                   "H": 17, "I": 34, "J": 18, "K": 19, "L": 20, "M": 21, "N": 22,
                   "O": 35, "P": 23, "Q": 24, "R": 25, "S": 26, "T": 27, "U": 28,
                   "V": 29, "W": 32, "X": 30, "Y": 31, "Z": 33}

    n = letter_dict[id_list[0]]
    x = n // 10
    y = n % 10

    value = x * 1 + y * 9

    for i in range(1, 9):
        value += id_list[i] * (9-i)
    last_num = 10 - (value % 10)

    return last_num





if __name__ == '__main__':
    id = []
    id_string = ''
    letter = generate_letter()
    id.append(letter)
    first_num = generate_first_number()
    id.append(first_num)
    second_to_seventh_num = generate_second_to_seventh_number()
    for n in second_to_seventh_num:
        id.append(n)
    last_num = generate_last_number(id)
    id.append(last_num)

    for el in id:
        id_string += str(el)

    print(id_string)

    # generate_letter()