# Show case
#
# @Author: Afonso Rafael & Renata
#
# Show case of the neural networks that
# where trained on the presented data.
# It's not a very versatile "main" file... it's
# literally just a showcase the work done
# until now.

from NN import utils as ut
from Games import connect4 as c4
from Games import tic_tac_toe as tic

# Libraries used are the libraries
# that where developed by us.

loop = True

ut.clear()
print(" " + 40*"-")
print("    Neural Networks On Strategy Games!")
print(" " + 40*"-")
print("\n\n")
print("1. To play Tic Tac Toe")
print("2. To play Connect Four")
print("3. To simulate games")
print()
print("Use \'clear\' to clean the terminal")
print("To print help press (h)")
print("To quit press (q)")

while(loop):
    command = input(
        "> ")

    if command == "q":
        loop = False

    elif command == "1":
        tic.play("nn", "p", nn_file="Trained_NN/MLP_Tic_Tac_Toe")

    elif command == "2":
        c4.play("nn", "p", nn_file="Trained_NN/MLP_Connect4")

    elif command == "3":
        ut.clear()
        print("Simulating Games...")
        print()
        print("Making our Tic Tac Toe neural network play")
        print("against a random player a 1000 times!")
        print()
        print("This will take a couple of seconds...")
        print()
        tic.simulate_games(1000, player1_mode="nn",
                           player2_mode="r",
                           nn_file="Trained_NN/MLP_Tic_Tac_Toe")
        print()
        input("[Press Enter to continue]")
        print()
        print("Making our Connect Four neural network play")
        print("against a random player a 1000 times!")
        print()
        print("This will take a couple of seconds...")
        print()
        c4.simulate_games(1000, player1_mode="nn",
                          player2_mode="r",
                          nn_file="Trained_NN/MLP_Connect4")

    elif command == "h":
        print()
        print("1. To play Tic Tac Toe (TTT)")
        print("2. To play Connect Four (C4)")
        print("3. To simulate games (s)")
        print()
        print("Use \'clear\' to clean the terminal")
        print("To print help press (h)")
        print("To quit press (q)")

    elif command == "clear":
        ut.clear()
