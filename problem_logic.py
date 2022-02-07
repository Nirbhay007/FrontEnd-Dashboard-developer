board_size = 4  # it could be changed later if we want
board = [[0, 0, 2, 4], [2, 4, 0, 0], [2, 0, 0, 4], [4, 4, 4, 2]]


def display_board(board):

    maximum = board[0][0]
    for row in board:

        for element in row:
            if(element > maximum):
                maximum = element
    for row in board:
        current_Row = "╏ "

        for element in row:
            if(element == 0):
                current_Row += (len(str(maximum))*"  "+"╏ ")
            else:
                current_Row += ((len(str(maximum))-len(str(element)))*"  " +
                                str(element)+" ╏ ")
        print(current_Row)
        print("-"*maximum*(board_size+1))
    print()


display_board(board)
