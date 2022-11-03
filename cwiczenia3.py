# https://github.com/krzysztofmakuch/pythonProgramming/projects/3

# formatting data
'''print('%.1f' % (3.1426))
lista = ['Ala', 'Marek', 'Kunegunda', 'Zosia']
for elem in lista:
    print('%10s' % (elem))'''

# dicts
'''uczniowie = {'id1': 'Tomek', 'id2': 'Aga'}
print(uczniowie['id1'])
uczniowie['id3'] = 'Izydor'
uczniowie.pop('id2')
print(uczniowie)'''


# 1
def converter(kg):
    return '%.1f' % (kg*2.205)


# 2
def is_string_numbers(string):
    try:
        int(string)
        if int(string) > 0:
            return True
        else:
            return False
    except ValueError:
        return False


def is_string_floats(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


# 3
def second_elements(lista):
    for elem in lista:
        print(elem[1])


# 4
def print_sublists(lista):
    for elem in lista:
        print('%.1s : %.3s' % (elem[0], elem[1]))


# 5
lista1 = [4, 1, 612]
lista2 = lista1
lista2[1] = 2
# print(lista1, lista2)  # lists are identical
# ???

# 6
'''L = {'id1': [3, 5], 'id2': [9, 18]}
print(dir(L))
print(L.keys())
print(L.values())
# print(L['id1'], L['zlyklucz']) - KeyError
print(L.get('id1'), L.get('zlyklucz'))
L.update({'id3': [7, 35]})
L['id4'] = [16, 64]
L.__delitem__('id2')
L.pop('id1')
print(L)'''


# 7
def dict_from_list(lista):
    dictionary = {}
    for elem in lista:
        dictionary.update({elem[0]: elem[1]})
    return dictionary


def dict_from_list2(lista):
    dictionary = {elem[0]: elem[1] for elem in lista}
    return dictionary


# 8 - nie rozumiem polecenia

# 9
def is_palindrome(string):
    return string == string[::-1]


# 10 multiplying matrices, kill me
def multiplying_matrices(matrix_a, matrix_b):
    dim_rows = len(matrix_a)
    dim_cols = len(matrix_b[0])
    matrix_c = []
    # filling with zeroes
    for elem in range(dim_rows):
        row = []
        for num in range(dim_cols):
            row.append(0)
        matrix_c.append(row)
    # filling with actual answers
    for elem in range(dim_rows):
        for num in range(dim_cols):
            for i in range(len(matrix_b)):
                matrix_c[elem][num] += matrix_a[elem][i] * matrix_b[i][num]
    return matrix_c


# 11
def swap(arg1, arg2):
    tmp = arg1
    arg1 = arg2
    arg2 = tmp
    return arg1, arg2


def bubble_sort(lista):
    length = len(lista)
    while length > 1:
        for i in range(0, length-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = swap(lista[i], lista[i+1])
        length = length - 1
    return lista
