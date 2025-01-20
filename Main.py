from Buffer import File
from Parser import Node, initialize_parse, print_tree, evaluate, globals
from Helper import *

introduction()

number_chosen = 0

print("\n")

while True:
    print("Enter The number of the instruction you want to operate.\n")
    print("1. Enter the File Name. \n")
    print("2. Exit. \n")
    number_chosen = int(input("Enter the number: "))
    if number_chosen == 1:
        file_name = input("Enter the file name: ")
        inputFile = File(file_name + ".txt")
        input_tokens = inputFile.read_from_file()
        initialize_parse(input_tokens)
        tree = Node().G()
        if not globals['error']:
            print_tree(tree)
            value = evaluate(tree)
            print("The calculated value is " + str(value))
        else:
            print("Unsuccessful parsing!!")
        print("\n")
    elif number_chosen == 2:
        print("The system has been logged out.")
        end_the_program()
    else:
        print("Invalid input!! Try again later.\n")
