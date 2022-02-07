import random
import copy


board_size = 4  # it could be changed later if we want
board = [[0, 0, 2, 4], [2, 4, 0, 0], [2, 0, 0, 4], [4, 4, 4, 2]]


def display_board(board):

    maximum = board[0][0]
    for row in board:

        for element in row:
            if(element > maximum):
                maximum = element

    spaceLength = len(str(maximum))
    for row in board:
        current_Row = "╏"

        for element in row:
            if(element == 0):
                current_Row += (spaceLength*" "+" ╏ ")
            else:
                gap = spaceLength-len(str(element))
                current_Row += (gap*" " +
                                str(element)+" ╏ ")
        print(current_Row)
        print("-"*(spaceLength+2)*(board_size+1))
    print()


display_board(board)

# This function will be used for merging one row to the left


def mergeOneRowLeft(row):
        # move everything to the left

    for j in range(board_size-1):
        for i in range(board_size-1, 0, -1):
                # testing for any empty spaces,move ahead if there is

            if(row[i-1] == 0):
                row[i-1] = row[i]
                row[i] = 0
    # merging everything to their left side
    for i in range(board_size-1):
            # checking if the value of the element is same as the element ahead of it
        if(row[i] == row[i+1]):
                # if true then multiplying by 2 and keeping the other element as 0
            row[i] *= 2
            row[i+1] = 0

    for i in range(board_size-1, 0, -1):
        if(row[i-1] == 0):
            row[i-1] = row[i]
            row[i] = 0
    return row


# This function is going to merge whole board to the left side
def merge_left(currentBoardStatus):
        # Merge every row in the board to the left
    for i in range(board_size):

        currentBoardStatus[i] = mergeOneRowLeft(currentBoardStatus[i])

    return currentBoardStatus


# This function is used for reversing the order of each row
def reverse(row):
        # Adding all the elements of the row to a new list in reverse order
    new_list = []
    for i in range(board_size-1, -1, -1):
        new_list.append(row[i])
    return new_list


# This function is going to merge the board to the right
def merge_right(currentBoardStatus):
        # Looking at every row in the board
    for i in range(board_size):
                # Reverse the row and merge to the left, then reverse again
        currentBoardStatus[i] = reverse(currentBoardStatus[i])
        currentBoardStatus[i] = mergeOneRowLeft(currentBoardStatus[i])
        currentBoardStatus[i] = reverse(currentBoardStatus[i])

    return currentBoardStatus


# This function is going to give us the transpose of the board
def transpose(currentBoardStatus):
    for row in range(board_size):
        for col in range(row, board_size):
            if(row != col):
                temp = currentBoardStatus[row][col]
                currentBoardStatus[row][col] = currentBoardStatus[col][row]
                currentBoardStatus[col][row] = temp

    return currentBoardStatus


# This function is going to merge the board in the upward direction
def merge_top(currentBoardStatus):
        # transpose the whole board then merge to the left then transpose back
    currentBoardStatus = transpose(currentBoardStatus)
    currentBoardStatus = merge_left(currentBoardStatus)
    currentBoardStatus = transpose(currentBoardStatus)

    return currentBoardStatus


# This function is going to merge the board to the bottom
def merge_bottom(currentBoardStatus):
        # Transposes the whole board,merging to the right then transposing back again
    currentBoardStatus = transpose(currentBoardStatus)
    currentBoardStatus = merge_right(currentBoardStatus)
    currentBoardStatus = transpose(currentBoardStatus)

    return currentBoardStatus


# This function picks a random value for the board between 2 and 4
def pickRandomValue():
    return random.choice([2, 4])

# This function is going to add a new value to the board in any empty spaces


def addValue():
    rowValue = random.randint(0, board_size-1)
    colValue = random.randint(0, board_size-1)

    # Picking the spots until we find one thats empty
    while(not board[rowValue][colValue] == 0):
        rowValue = random.randint(0, board_size-1)
        colValue = random.randint(0, board_size-1)

    # filling the empty space with a new value
    board[rowValue][colValue] = pickRandomValue()


# This functions will check whether the user has won or not

def isWon():
    for row in board:
        if 2048 in row:
            return True
    return False


# This function is going to check for losses
def noMoves():
    pass


# Creating a blank board
board = []

for i in range(board_size):
    row = []

    for j in range(board_size):
        row.append(0)
    board.append(row)

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


gameEnded = False

# Keep asking the user for the new moves while the game is not over
while not gameEnded:
    move = int(input(
        "Which direction do you want to move? Press 1 for left 2 for right 3 for up and 4 for down. "))
  # Assuming the user entered a valid value for input

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


merge_left(board)
display_board(board)
transpose(board)
display_board(board)
merge_right(board)
display_board(board)
merge_top(board)
display_board(board)
merge_bottom(board)
display_board(board)
