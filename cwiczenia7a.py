# https://github.com/krzysztofmakuch/pythonProgramming/projects/7
import os
import re
import datetime

# pani Maria
os.chdir(r"C:\Users\Kasia\PycharmProjects\pythonProject\praca_z_plikami")
file_list1 = os.listdir(r"C:\Users\Kasia\PycharmProjects\pythonProject\praca_z_plikami")

day_file = lambda x: x in re.findall('..\...\.....\.txt', x)
file_list1 = list(filter(day_file, file_list1))


def count_clients(file_list):
    num_of_days = len(file_list)
    clients_total = [0 for i in range(8, 19)]
    for file in file_list:
        with open(file) as file_name:
            file_name.readline()  # skipping
            file_name.readline()  # skipping
            i = 0
            while True:
                line = file_name.readline()
                line = line.strip()
                if not line:
                    break
                line = line.split()
                clients_total[i] += int(line[1])
                i += 1
    clients_average = [client/num_of_days for client in clients_total]
    return clients_average


print(count_clients(file_list1))

# datetime module

# hour = datetime.datetime.now().strftime('%H')
def covert_str_to_date(string):
    return datetime.datetime.strptime(string, '%Y-%m-%d')


def convert_date_to_str(date):
    return date.strftime('%m/%d/%Y, %H:%M')


# your age
def your_age():
    age = input('Enter you date of birth using format dd/mm/yyyy: ')
    try:
        dob = datetime.datetime.strptime(age, '%d/%m/%Y')
        now = datetime.datetime.now()
        time_from_dob = now - dob
        print(time_from_dob)
    except ValueError:
        print('Make sure to use proper formatting!')
