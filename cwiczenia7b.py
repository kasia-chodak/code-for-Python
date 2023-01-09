# https://github.com/krzysztofmakuch/pythonProgramming/projects/7
import sys
import math

command_len = len(sys.argv)

command = ''
for i in range(1, command_len):
    command += sys.argv[i]

print(eval(command))


class Worker:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print('--WORKER INFO--')
        print('Worker name: ', self.name)


marek = Worker('Marek')
marta = Worker('Marta')
stefan = Worker('Stefan')
marek.display_info()


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def display_info(self):
        print('--INFORMATION ABOUT YOUR CYLINDER--')
        print('Base area: ', math.pi * self.radius * self.radius)
        print('Curved surface area: ', math.pi * 2 * self.radius * self.height)
        print('Volume: ', math.pi * self.radius * self.radius * self.height)
        print('Diagonal: ', math.sqrt((2*self.radius)**2 + self.height**2))


cylinder = Cylinder(3, 5)
cylinder.display_info()
