# https://github.com/krzysztofmakuch/pythonProgramming/projects/6
# https://docs.python.org/3/library/subprocess.html
import re
import glob
import os


# glob module
os.chdir(r"C:\Users\Kasia\PycharmProjects\pythonProject\os_folder")
print(glob.glob(r'*.txt'))
print(glob.glob(r'*[.]*'))


# os module

os.chdir(r"C:\Users\Kasia\PycharmProjects\pythonProject\os_folder")
file_list = os.listdir(r"C:\Users\Kasia\PycharmProjects\pythonProject\os_folder")

print(os.getcwd())
print(os.path.exists(r"C:\Users\Kasia\PycharmProjects\pythonProject\os_folder"))

with open('file_list.txt', 'w') as new_file:
    for elem in file_list:
        new_file.write(elem)
        new_file.write(', ')
        new_file.write(os.path.abspath(elem))
        new_file.write('\n')

# os.rename('file_list.txt', 'files_in_dir_list.txt')

list_txt = []
for elem in file_list:
    pattern = re.compile(r'.*.txt$')
    if re.match(pattern, elem):
        list_txt.append(elem)
print(list_txt)
# now it would be easy to change names for all .txt files having the list that contains all of them

print(os.listdir(r'C:\Users\Kasia\PycharmProjects\pythonProject'))


# 1
sequence_1 = "ATTTGGCGAGAGACATCATCATCAT"
repeats_itself = re.findall(r'(.+)\1\1', sequence_1)
print(repeats_itself)

# 2
phrase_2 = "Mam na imię AdamNowak."
phrase_2 = re.sub(r'([a-z])([A-Z])', r'\1 \2', phrase_2)
print(phrase_2)

# 3
phrase_3 = "DZisiaj jest czwartek. JUtro będzie piątek."
phrase_3 = re.sub(r'([A-Z])([A-Z])', lambda x: x.group(1)+x.group(2).lower(), phrase_3)
print(phrase_3)

# 4
phrase_4 = 'aldaAS dsADWF ADSshtKK. Gdwygh GIRT. fvrgoij muewrsd we. EEE.'
phrase_4 = re.sub(r'([A-Z])', lambda x: x.group(1).lower(), phrase_4)
phrase_4 = re.sub(r'(\.[ ])([a-z])', lambda x: x.group(1) + x.group(2).upper(), phrase_4)
phrase_4 = re.sub(r'(^[a-z])', lambda x: x.group(1).upper(), phrase_4)
print(phrase_4)

# 5
phrase_5 = '2019-11-28'
phrase_5 = re.sub(r'([0-9]{4})-([0-9]{2})-([0-9]{2})', lambda x: x.group(3) + "-" + x.group(2) + "-" + x.group(1), phrase_5)
print(phrase_5)
