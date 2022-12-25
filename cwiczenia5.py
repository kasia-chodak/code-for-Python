# https://github.com/krzysztofmakuch/pythonProgramming/projects/5
import re
import random

# 0
list_0 = [1, 2, 3, 4, 5]
random.shuffle(list_0)
# print(list_0)
# print(random.choice(list_0))


# 1
# tmp_1 = 5/0  # ZeroDivisionError
# tmp_2 = 'ala' + 2  # TypeError
# tmp_3 = [1,2,3][5]  # IndexError
# tmp_4  # NameError
# for i in range 5:
#    print(i)  # SyntaxError

# 2
'''
for i in range(-5, 6):
    try:
        result = 5/i
        print('Dzielenie liczby pięć przez %.f daje %.1f' % (i, result))
    except ZeroDivisionError:
        print('Nie dzielimy przez 0!')
'''

# 3
'''
while True:
    num = input("Enter natural number: ")
    try:
        num = float(num)
        if num == 0:
            break
        elif num < 0:
            raise ValueError
    except ValueError:
        print("You entered something else! Try again. ")
'''


# 4
def login(string):
    splitted = string.split()
    login = splitted[0][0] + splitted[1][0] + str(len(splitted[0])) + str(len(splitted[1]))
    return login


def make_logins(*names):  # * - krotka
    logins = []
    for name in names:
        logins.append(login(name))
    return logins


# print(make_logins('Marek Kowalski', 'Jan Gut', 'Anna Karenina', 'Yang Zgang'))

# 5
def is_rented(book_name, **kwargs):  # ** - dict
    list_of_id = []
    for elem in kwargs.keys():
        if book_name in kwargs[elem]:
            list_of_id.append(elem)
    return list_of_id


# print(is_rented('Ferdydurke', id1=['Potop', 'Pan Tadeusz'], id2=['Ferdydurke'],
# id3=['Zbrodnia i kara', 'Potop', 'Harry Potter']))
# print(is_rented('Pan Tadeusz', id1=['Potop', 'Pan Tadeusz'], id2=['Ferdydurke']))

# 6
class Employee:
    def __init__(self, name):
        self.name = name


mirek = Employee('Mirek')
stefan = Employee('Stefan')
marta = Employee('Marta')

# Zadanie1 - center module
'''
sequence = "ATGGAAGAAtcACAGGCAGAACTCAATG" \
   "tggAGCCCCCTCTGAGTCagGAGACATTttCCGACTTGTGGTGA"
sequence = sequence.upper()
sequence = sequence.replace('T', 'U')
print(sequence[:3] == 'AUG')
print(sequence[(len(sequence)-3):] == 'UGA' or
      sequence[(len(sequence)-3):] == 'UAA' or
      sequence[(len(sequence)-3):] == 'UAG')
print(sequence[3:(len(sequence)-3)])
print('CUC' in sequence)
print(sequence)
for ndx in range(len(sequence)-3):
    if sequence[ndx] == 'C' and ndx % 3 == 0:
        if sequence[ndx+1] == 'U' and sequence[ndx+2] == 'C':
            print('CUC is a codon')
            break
'''

# Zadanie2
# https://docs.python.org/3/library/re.html
# https://www.w3schools.com/python/python_regex.asp

# Zadanie3
'''
txt_31 = ['mama', 'mem', 'mom']
txt_32 = ['ac', 'abc', 'abbc', 'abbbc']
txt_33 = ['tab', 'teb', 'teab', 'teaab']
for elem in range(len(txt_31)):
    print(re.search('m.ma?', txt_31[elem]))
for elem in range(len(txt_32)):
    print(re.search('ab*c', txt_32[elem]))
for elem in range(len(txt_33)):
    print(re.search('t[ae]*b', txt_33[elem]))
'''

# Zadanie4
'''
txt_4 = 'ala'
print(re.search('^a.*', txt_4))
print(re.search('.*a', txt_4))
'''


# Zadanie5
def find_dates(string):
    return re.findall('[0-9]+', string)


story = 'Marie Sklodowska Curie (1867–1934) was the first person ever to receive two Nobel Prizes: the first in 1903' \
        ' in physics, shared with Pierre Curie (her husband) and Henri Becquerel for the discovery of the phenomenon' \
        ' of radioactivity, and the second in 1911 in chemistry for the discovery of the radioactive elements ' \
        'polonium and radium.'
# print(find_dates(story))


# Zadanie6
def del_lower(string):
    to_del = re.findall('[a-z]+', string)
    for elem in to_del:
        string = string.replace(elem, '')
    return string
#wydaje mi się, że szybciej byłoby zrobić find dużych i join, ale tak też jest ok

example = "ATTTGgccTaC"
# print(del_lower(example))


# Zadanie7
def find_emails(string):
    return re.findall('\w+@[a-z]*\.[a-z]+', string)


txt_7 = 'ala ma kota: ala@interia.pl ola hahaha@wp.pl grzes nie ma pk81@gmail.com'
# print(find_emails(txt_7))


# Zadanie8
def is_same_letter(lista):
    lista_double_letters = []
    for elem in lista:
        pattern = re.compile(r'^(.)[a-zA-Z]+[ ]\1.*$')
        if re.match(pattern, elem):
            lista_double_letters.append(elem)
    return lista_double_letters


L = ["Adam Nowak", "Kasia Klimczak", "Maria Rudzik"]
# print(is_same_letter(L))
