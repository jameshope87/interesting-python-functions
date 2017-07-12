ord = {'a': 3, 'b': 25, 'c': 14, 'd': 9, 'e': 1, 'f': 13, 'g': 26, 'h': 20}

def find_num(string):
    num_list = []
    for i in string:
        num_list.append(ord[i])
    return num_list

def find_letter(number):
    for i in ord:
        if ord[i] == number:
            return i

def xoradd(a, b):
    num_list_a = find_num(a)
    num_list_b = find_num(b)
    for (i, j) in zip(num_list_a, num_list_b):
        s = ''.join(find_letter(i ^ j))
    return s


