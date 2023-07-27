from random import randrange


def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def enter_move(board):
    ok = False  # getting in the loop
    while not ok:
        move = input("Enter your move: ")
        ok = len(move) == 1 and move >= "1" and move <= "9"  # is it valid?
        if not ok:
            print("Wrong move, try again")  # no, it's not
            continue
        move = int(move) - 1  # field number, 0-8
        row = move // 3  # field row
        col = move % 3  # field column
        sign = board[row][col]  # puts the mark on the board
        ok = sign not in ["O", "X"]
        if not ok:  # the field is marked, try again
            print("This field is marked, try again!")
            continue
    board[row][col] = "O"  # puts '0' on the selected field


def free_fields(board):
    free = []  # empty list
    for row in range(3):  # loop through the rows
        for col in range(3):  # loop through the comlumns
            if board[row][col] not in ["O", "X"]:  # is the field empty?
                free.append((row, col))  # yes, appends a new tuple to the list
    return free


def victory(board, sgn):
    if sgn == "X":  # is there an 'X'?
        who = "machine"  # is the program
    elif sgn == "O":  # is there a '0'?
        who = "you"  # is the user
    else:
        who = None  # we shouldn't get here...
    cross1 = cross2 = True
    for rc in range(3):
        if (
            board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn
        ):  # check row rc
            return who
        if (
            board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn
        ):  # check column rc
            return who
        if board[rc][rc] != sgn:  # check first cross
            cross1 = False
        if board[2 - rc][2 - rc] != sgn:  # check second cross
            cross2 = False
    if cross1 or cross2:
        return who
    return None


def draw_move(board):
    free = free_fields(board)  # new list with empty fields
    check_field = len(free)
    if check_field > 0:  # if the list is not empty, choose a place for 'X' and put it
        this = randrange(check_field)
        row, col = free[this]
        board[row][col] = "X"


board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]  # create a new board
board[1][1] = "X"  # first 'X' in the center field
free = free_fields(board)
human_turn = True  # who's next?
while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory(board, "O")
    else:
        draw_move(board)
        victor = victory(board, "X")
    if victor != None:
        break
    human_turn = not human_turn
    free = free_fields(board)

display_board(board)
if victor == "you":
    print("You win!")
elif victor == "machine":
    print("I win!")
else:
    print("It's a tie!")
