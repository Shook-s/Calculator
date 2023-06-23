# Calculator

import math

print("hi this is a calculator by shook-s")

def mode_1():
    equation = input("Enter the equation: ")
    try:
        result = eval(equation)
        print(result)
    except Exception as e:
        print("Error:", str(e))


def mode_2():
    print("\nAddition represented by +"
          "\nSubtraction represented by -"
          "\nMultiplication represented by *"
          "\nDivision represented by /\n")

def mode_3():
    print("\nUsing this calculator program is very simple")
    print("All that you've got to do is choose a number and the arithmetic function that you want to use")
    print("Currently you can use function at a time but in the future I hope to change that\n")

def mode_4():
    print("Bye bye")
    exit()


def modes():
    while True:
        try:
            choose_mode = int(input(
                "choose what you want to do"
                "\n[1] Calculate"
                "\n[2] Funtions"
                "\n[3] How to use"
                "\n[4] Exit\n"
                ))
            if choose_mode in [1,2,3,4]:
                mode_selection = {
                    1 : mode_1,
                    2 : mode_2,
                    3 : mode_3,
                    4 : mode_4,
                }
                selected_mode = mode_selection[choose_mode]
                selected_mode()
            else:
                print("Pick a number bewteen 1-4")
        except ValueError:
            print("Error choose a number")

modes()