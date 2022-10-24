# https://github.com/krzysztofmakuch/pythonProgramming/projects/2
import math
from tabulate import tabulate


def parity(number):
    if number % 2 == 0:
        return True
    else:
        return False


def write_numbers_while(fromm, too):
    while fromm < too:
        print(fromm)
        fromm = fromm + 1


def write_numbers_for(fromm, too):
    for number in range(fromm, too):
        if not parity(number):
            print(number)


def the_letter(string, ndx):
    return string[ndx]

"""
lista = []
for num in range(3, 6):
    lista.append(num)

i = 0
while i < len(lista):
    print(lista[i])
    i = i + 1

a = "ala"
b = "kot"
print(a + b)
print(3 * a)
print(a, b)

print(the_letter(a, 1))

c = a + " " + b
print(c)
c_list = list(c)

c_list.pop()
c_list.pop()
c_list.pop()
c_list.append("p")
c_list.append("i")
c_list.append("e")
c_list.append("s")
print(c_list)
c = c.split()[0]
print(c.upper())
"""


def delete_as(string):
    string = list(string)
    if "a" not in string:
        return string
    else:
        counter = 0
        for letter in string:
            if letter == "a":
                counter = counter + 1
        while counter > 0:
            counter = counter - 1
            string.remove("a")
        return string


# print(delete_as("ala ma kota"))


def exclamation(string):
    counter = 0
    for letter in string:
        if letter == "!":
            counter = counter + 1
    string = string[:len(string)-counter]
    string = string + "!"*counter*3
    return string


# print(exclamation("Cześć!!"))


def login(string):
    splitted = string.split()
    login = splitted[0][0] + splitted[1][0] + str(len(splitted[0])) + str(len(splitted[1]))
    return login


def angles(angle):
    rad_angle = angle*math.pi/180
    cos_angle = math.cos(rad_angle)
    sin_angle = math.sin(rad_angle)
    angle_table = [["angle [deg]", angle], ["angle [rad]", rad_angle], ["sin(angle)", sin_angle], ["cos(angle)", cos_angle]]
    return angle_table


angl = 60
print(tabulate(angles(angl), tablefmt="github"))
