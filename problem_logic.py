

def display_board():


def create_board():

    size = 4
    board = []

    for row in range(size):
        row = []
        for element in range(size):

            row.append(0)

        board.append(row)

    print(board)


create_board()
