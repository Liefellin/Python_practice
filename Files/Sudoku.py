# Zala Weyker
# 9/10/1023
# Sudoku
# This task will read a file containing a 9x9
# sudoku matrix and output True if it is valid,
# False if it is not.


def sudoku_file_to_board(filename):
    """Reads a file formatted for this
     exercise and outputs a "board". In this case,
      a board is a nested list of every number in every row.

    Example:
     [
     [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]"""
    with open(filename, 'r') as sudoku_file:
        board = []
        for line in sudoku_file:
            row = []
            for character in line.strip():
                row.append(character)
            board.append(row)
        return board


def sudoku_board_to_rows(board):
    """This function takes a board and reformats it into a row-focused dictionary.

    Example:
        {
            1: [1, 2, 3, 4, 5, 6, 7, 8, 9],
            2: [1, 2, 3, 4, 5, 6, 7, 8, 9],
            3: [1, 2, 3, 4, 5, 6, 7, 8, 9],
            4: [1, 2, 3, 4, 5, 6, 7, 8, 9],
            5: [1, 2, 3, 4, 5, 6, 7, 8, 9],
            6: [1, 2, 3, 4, 5, 6, 7, 8, 9],
            7: [1, 2, 3, 4, 5, 6, 7, 8, 9],
            8: [1, 2, 3, 4, 5, 6, 7, 8, 9],
            9: [1, 2, 3, 4, 5, 6, 7, 8, 9]
        }"""
    rows = {}
    for counter, row in enumerate(board):
        rows[counter] = row
    return rows


def sudoku_board_to_columns(board):
    """This function takes a board and reformats it into a column-focused dictionary.

Example:
    {
    1: [1, 1, 1, 1, 1, 1, 1, 1, 1],
    2: [2, 2, 2, 2, 2, 2, 2, 2, 2],
    3: [3, 3, 3, 3, 3, 3, 3, 3, 3],
    4: [4, 4, 4, 4, 4, 4, 4, 4, 4],
    5: [5, 5, 5, 5, 5, 5, 5, 5, 5],
    6: [6, 6, 6, 6, 6, 6, 6, 6, 6],
    7: [7, 7, 7, 7, 7, 7, 7, 7, 7],
    8: [8, 8, 8, 8, 8, 8, 8, 8, 8],
    9: [9, 9, 9, 9, 9, 9, 9, 9, 9]
    }"""
    columns = {}
    for rownum, row in enumerate(board):
        for columnnum, digit in enumerate(row):
            if columnnum not in columns:
                columns[columnnum] = [digit]
            else:
                columns[columnnum].append(digit)
    return columns


def sudoku_board_to_subsquares(board):
    """This function takes a board and reformats it into a subsquare-focused dictionary. The subsquares are read in standard reading order: left to right, down one line.

Example:
    {
    1: [1, 2, 3, 1, 2, 3, 1, 2, 3],
    2: [4, 5, 6, 4, 5, 6, 4, 5, 6],
    3: [7, 8, 9, 7, 8, 9, 7, 8, 9],
    4: [1, 2, 3, 1, 2, 3, 1, 2, 3],
    5: [4, 5, 6, 4, 5, 6, 4, 5, 6],
    6: [7, 8, 9, 7, 8, 9, 7, 8, 9],
    7: [1, 2, 3, 1, 2, 3, 1, 2, 3],
    8: [4, 5, 6, 4, 5, 6, 4, 5, 6],
    9: [7, 8, 9, 7, 8, 9, 7, 8, 9]
    }"""
    subsquares = {}
    for rownum, row in enumerate(board):
        for columnnum, digit in enumerate(row):
            match columnnum, rownum:
                case _ if 3 > columnnum and 3 > rownum:
                    category = 1
                    if category not in subsquares:
                        subsquares[category] = [digit]
                    else:
                        subsquares[category].append(digit)
                case _ if 6 > columnnum >= 3 > rownum:
                    category = 2
                    if category not in subsquares:
                        subsquares[category] = [digit]
                    else:
                        subsquares[category].append(digit)
                case _ if 9 > columnnum >= 6 and 3 > rownum:
                    category = 3
                    if category not in subsquares:
                        subsquares[category] = [digit]
                    else:
                        subsquares[category].append(digit)
                case _ if columnnum < 3 <= rownum < 6:
                    category = 4
                    if category not in subsquares:
                        subsquares[category] = [digit]
                    else:
                        subsquares[category].append(digit)
                case _ if 3 <= columnnum < 6 and 3 <= rownum < 6:
                    category = 5
                    if category not in subsquares:
                        subsquares[category] = [digit]
                    else:
                        subsquares[category].append(digit)
                case _ if 9 > columnnum >= 6 > rownum >= 3:
                    category = 6
                    if category not in subsquares:
                        subsquares[category] = [digit]
                    else:
                        subsquares[category].append(digit)
                case _ if columnnum < 3 and 9 > rownum >= 6:
                    category = 7
                    if category not in subsquares:
                        subsquares[category] = [digit]
                    else:
                        subsquares[category].append(digit)
                case _ if 3 <= columnnum < 6 <= rownum < 9:
                    category = 8
                    if category not in subsquares:
                        subsquares[category] = [digit]
                    else:
                        subsquares[category].append(digit)
                case _ if 9 > columnnum >= 6 and 9 > rownum >= 6:
                    category = 9
                    if category not in subsquares:
                        subsquares[category] = [digit]
                    else:
                        subsquares[category].append(digit)
    return subsquares


def compile_text(text):
    """This function is loaned from another program. It determines what characters an iterable has and in what number."""
    letters = {}
    for character in text:
        if character.isalnum():
            if character in letters:
                letters[character] += 1
            else:
                letters[character] = 1
    return letters


def sudoku_quick_line_check(listy):
    """This function determines whether the given list has one and only one of each number up to 9"""
    correct_sudoku_line = sorted(list("123456789"))
    return sorted(listy) == correct_sudoku_line


def sudoku_is_focus_valid(focus):
    """This function looks at a dictionary as generated by one of the functions above and determines if this aspeect of the sudoku is valid"""
    for line in focus:
        if sudoku_quick_line_check(focus[line]):
            pass
        else:
            return False
    return True


def is_this_sudoku_valid_9x9(sudokufile):
    """This function combines the previous functions to achieve the stated goal of the program."""
    board = sudoku_file_to_board(sudokufile)
    return sudoku_is_focus_valid(sudoku_board_to_rows(board)) and sudoku_is_focus_valid(sudoku_board_to_columns(board)) and sudoku_is_focus_valid(sudoku_board_to_subsquares(board))


print(is_this_sudoku_valid_9x9('Sudoku_input_1'), is_this_sudoku_valid_9x9('Sudoku_input_2'), is_this_sudoku_valid_9x9('Sudoku_input_test'))
