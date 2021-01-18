import utils as ut
import numpy as np
import connect4 as c4
import tic_tac_toe as tic
import games_generator as gg

loop = True

ut.clear()
print(" " + 40*"-")
print("    Neural Networks On Strategy Games!")
print(" " + 40*"-")
print("\n\n")
print("1. To play Tic Tac Toe (TTT)")
print("2. To play Connect Four (C4)")
print()
print("To print help press (h)")
while(loop):
    command = input(
        "> ")

    if command == "q":
        loop = False

    if command == "h":
        print()
        print("1. To play Tic Tac Toe (TTT)")
        print("2. To play Connect Four (C4)")
        print()
        print("To print help press (h)")

    if command == "clear":
        ut.clear()
