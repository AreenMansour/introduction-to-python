import sys

from helper import *
from car import *

from board import *

valid_names = {"Y", "B", "O", "G", "W", "R"}
valid_movkeys = {"u", "d", "r", "l"}


class Game:
    """
    Add class description here
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        self.__board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code here (and then delete the next line - 'pass')
        pass

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        # implement your code here (and then delete the next line - 'pass')
        while self.__board.cell_content((3, 7)) == None:
            print(self.__board)
            user_input = input()
            if user_input == "!":
                return
            if len(user_input) != 3:
                print("please enter a valid input!")
                continue
            if user_input[0] not in valid_names:
                print("please enter a valid car name!")
                continue
            if user_input[2] not in valid_movkeys:
                print("please enter a valid move key!")
                continue
            car_name = user_input[0]
            movekey = user_input[2]
            self.__board.move_car(car_name, movekey)


if __name__ == "__main__":
    # Your code here
    # All access to files, non API constructors, and such must be in this
    # section, or in functions called from this section.

    d = load_json(sys.argv[1])
    board = Board()
    for n in d:
        if n in valid_names:
            length = d[n][0]
            location = d[n][1]
            orientation = d[n][2]
            if 2 <= length <= 4 and orientation in [0, 1]:
                car = Car(n, length, location, orientation)
                board.add_car(car)
    game = Game(board)
    game.play()
