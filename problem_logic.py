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


merge_left(board)
display_board(board)
transpose(board)
display_board(board)
merge_right(board)
display_board(board)
