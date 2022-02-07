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
        current_Row = "╏ "

        for element in row:
            if(element == 0):
                current_Row += (spaceLength*"  "+"╏ ")
            else:
                gap = spaceLength-len(str(element))
                current_Row += (gap*"  " +
                                str(element)+" ╏ ")
        print(current_Row)
        print("-"*board_size*(board_size))
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


merge_left(board)
display_board(board)
