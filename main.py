
from problem_logic import *
import copy


# Filling two spots with random values at the start of the game
numberNeeded = 2


while(numberNeeded > 0):

    randomRow = random.randint(0, board_size-1)
    randomCol = random.randint(0, board_size-1)
    if(board[randomRow][randomCol] == 0):
        board[randomRow][randomCol] = pickRandomValue()
        numberNeeded -= 1


print('''This is the 2048 game ! In this game your goal is to combine values
to get the number 2048, by merging the board in different directions.
You will have to press either  1, 2, 3 or 4 for left, right, up and down movements
\n\nHere is the starting board for you to start playing....\n''')

display_board(board)
gameEnded = False


# Keep asking the user for the new moves while the game is not over
while not gameEnded:

    try:
        move = int(input(
            "\nWhich direction do you want to move? Press 1 for left 2 for right 3 for up and 4 for down. Press 9 to quit.\n"))
     # Assuming the user entered a valid value for input
    except:
        move = 0

    if(move == 9):

        break
    validInput = True

    # creating a  new copy of the board which is going to be the same so deepcopy
    temporaryBoard = copy.deepcopy(board)

   # Finding whether the input was valid or not and use the correct move function
    if move == 1:
        board = merge_left(board)

    elif move == 2:
        board = merge_right(board)

    elif move == 3:
        board = merge_top(board)

    elif move == 4:
        board = merge_bottom(board)

    else:
        validInput = False
    # if the input was invalid,the user need to enter a new input
    if not validInput:
        print("Kindly press valid input , please try again..")
 # otherwise the user input was valid
    else:
        # Checking if the board is still equal to the temporary board which we created earlier
        if(board == temporaryBoard):
            # telling the user to try again
            print("Pleas try moving in different direction")

        else:
            # checking if the user has won
            if isWon():
                display_board(board)
                print("\nYou won!!!!!\n")
                gameEnded = True
            addValue()

            display_board(board)

            # Checking for the loss
            if isLoss():
                print("\nSorry ther is no any move left.\n")
                gameEnded = True
