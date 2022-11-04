# https://github.com/krzysztofmakuch/pythonProgramming/projects/4
from tabulate import tabulate
import math

# 0
power = lambda x: x**x
divisible = lambda x: (x % 3 == 0 & x % 7 == 0)

lista_0 = [['Ania', 2], ['Michal', 3], ['Romek', 3], ['Tysia', 1]]
dummy = lambda students: sorted(students, key = lambda x: x[1])
# print(dummy(lista_0)[1])

# 1
codes = ['ATTGC', 'AGGC', 'TTTGC']
number_of_T = lambda x: x.count('T')
result_1 = list(map(number_of_T, codes))

# 2
sequences = ['ATGCC', 'TATC', 'GGATGGGG']
length = lambda x: len(x) > 4
result_2a = list(filter(length, sequences))

seq_TC = lambda x: x.__contains__('TG')  # or 'TG' in x
result_2b = list(filter(seq_TC, sequences))

codons = ["ATCGGGCAT", "ATCGA", "TTTGCGA"]


def deletions(lista_2):
    deletion = lambda code: len(code) % 3 != 0
    return list(filter(deletion, lista_2))


# 3
list(map(lambda x: x**x, [1, 2, 3, 4, 5, 6]))
lista_3 = [x**x for x in range(1, 7)]

# 4
s = "UGAGGUAGUAGGUUUUUUUUUU, " \
    "UGAGGUAGUAGGUUGAUUUUUU, " \
    "UGAGGUAGUAGGUUGUUUUUUU, " \
    "UGAGGUAGUAGGUUGUGAUUUU, " \
    "UGAGGUAGUAGGUUGUAUGGUU"


def uracils(string):
    list_4 = string.split(',')
    list_4.sort(key = lambda x: x.count('U'))
    return list_4


# 5
with open('pracownicy.txt', 'r') as file1:  # extracting data from file - ID, Surname, Salary
    employers = []
    line_num = 1
    for line in file1:
        line = line.split(';')
        line[3] = line[3].replace('\n', '')
        employers.append([line[0].replace(' ', ''), line[2].replace(' ', ''), line[3].replace(' ', '')])
        line_num += 1

employers.remove(['ID', 'NAZWISKO', 'PLN'])  # removing headers
sum = 0

for ndx in range(len(employers)):
    employers[ndx][2] = int(employers[ndx][2])
    sum += employers[ndx][2]
# print(tabulate(employers))
# print('Sum of salaries: %s' % sum)


# 6
def pracownicy(lista_1):
    while True:
        command = input('Enter your command: ')
        if command == '1':
            for idx in range(len(lista_1)):
                print(lista_1[idx][1])
        elif command == '2':
            identificator = input('Enter id: ')
            money = input('Enter new salary: ')
            lista_1[int(identificator)-1][2] = money
        elif command == '3':
            new_name = input('Enter new file name:')
            with open(new_name, 'w') as new_file:
                for idx in range(len(lista_1)):
                    new_file.write(str(lista_1[idx]))
                    new_file.write('\n')
            return 'All done!'
        else:
            print('Invalid command')


# 7
result = (math.sin(math.pi/4) + math.factorial(6))/(math.e**4 + math.log(5))
