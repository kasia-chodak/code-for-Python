# https://github.com/krzysztofmakuch/pythonProgramming/projects/1

print(1 + 1 + 1)  # ints are precise
print(0.1 + 0.1 + 0.1)  # floats are not D:

print(round(3.1414, 2))
print(round(2.6, 0))
print(int(2.6))
print(bin(5))


def hexadecimal(number):  # converting to hexadecimal
    number = hex(number)
    return number


your_number = int(input("Enter your number: "))
print(hexadecimal(your_number))


def calculator(func, number):
    if func == "binary":
        return bin(number)
    elif func == "hexadecimal":
        return hex(number)
    elif func == "div_2":
        if number % 2 == 0:     #ten if else i nastepy mozna krocej: return number %2 == 0
            return True
        else:
            return False
    elif func == "div_7":
        if number % 7 == 0:
            return True
        else:
            return False
    else:
        return "Invalid func"


print(calculator("binary", 8))
print(calculator("hexadecimal", 32))
print(calculator("div_2", 7))
print(calculator("div_7", 7))


def BMI(heights, weights):
    bmi = weights/(heights**2)
    bmi = round(bmi, 1)
    print(bmi)
    if bmi < 18.5:
        print("You are underweight :(")
    elif bmi < 23:
        print("You are within normal range!")
    elif bmi < 25:
        print("You are overweight and at risk of obesity.")
    elif bmi < 30:
        print("You are moderately obese.")
    else:
        print("You are severely obese!")


height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
BMI(height, weight)
