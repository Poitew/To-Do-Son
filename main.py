import os
from art import tprint
from sys import exit
from functions_menu import AddTask, DeleteTask, ViewJson

try:
    width, height = os.get_terminal_size(0)
except OSError:
    width = 20
    
half_width = int(width / 2)

separator = "=" * width
title = "To-Do-Son"
title = title.center(half_width)
menu = {
    "1": "Add Task",
    "2": "Delete Task",
    "3": "View Json",
    "4": "Exit"
}

def main():

    print(separator)
    tprint(title)

    # for each pair in menu we get the index and the option itself, we then display both of them.
    # the text is centered by putting a padding left on the keys which moves the options too -> index.rjust(int(half_width / 2))
    for index, element in menu.items():
        print(index.rjust(int(half_width / 2)), element)

    menu_input = input("What would you like to do? (1 - 4): ")

    match menu_input:
        case "1":
            AddTask()
        case "2":
            DeleteTask()
        case "3":
            ViewJson()
        case "4":
            exit(0)
        case _:
            print("Wrong option")


if __name__ == "__main__":
    while True:
        main()