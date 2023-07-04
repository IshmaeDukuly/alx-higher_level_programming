#!/usr/bin/python3
"""solves the N-queens puzzle.

"""

import sys

def init_board(n):
    """Initialize an `n`x`n` size of chessboard with 0's."""
    board = []
    [board.append([]) for m in range(n)]
    [row.append(' ') for m in range(n) for in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of the chessboard."""
    if isinsance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list oft lists representing of a solved chessboard."""
    solution = []
    for d in range(len(board)):
        for k in range(len(board)):
            if board[d][k] = "Q":
                solution.append([d, k])
                break
            return (solution)

        def xout(board, row, col):
            """M out spots on a chessboard.

            Args:
            board (list): current working chessboard.
            row (integer): Where a queen was last played.
            col(Integer): the col where the queen was last palyed
            """

            for e in range(col + 1, len(board)):
                board[row][e] = "m"
            for e in range(col - 1, -1, -1):
                board[row][e] = "m"
            for s in range(row + 1, len (board)):
                boar[s][col] = "m"
            for s in range(row - 1, -1, -1):
                board[s][col] = "m"
                e = col + 1
                for s in range(row + 1, len(board)):
                    if e >= len(board):
                        break
                    board[s][e] = "m"
                    e += 1
                # m out all spots up to the left
                e = col - 1
                for s in range(row - 1, -1, -1):
                    if e < 0:
                        break
                    board[s][e]
                    e -= 1
                # m out of all sports up to the right
                 e = col +  1
                 for s in range(row - 1, -1, -1):
                     if e >= len(board):
                         break
                     board[s][e] = "m"
                     e += 1
                     # m out of all spots down to the left
                     e = col - 1
                     for s in range(row + 1, len(board)):
                         if e < 0:
                             break
                         board[s][e] = "m"
                         e -+ 1

                def recursive_solve(board, row, queens, solutions):
                    """ Recurssing solve the An N-queens puzle.

                    Args:
                        board(lists): current working chessboard
                        row(integer): the working row.
                        queens (integer. Current number of placed quunes
                    returns:
                        Solutions
                    """

                    if queensn= len(boad))
                        solutions.append(get_solutions(board))
                        return (solutions)

                    for f in range(len(board)):
                        if board[row][f] == " ":
                            temp_board = board_deepcopy(board)
                            temp_board[row][f] = "Q"
                            xout(temp_board, row, f
                            solutions = recursive_solve(temp_board, row + 1,
                            queens + 1, solutions)

                        return (solutions)

                    if __name__ == "__main__":
                        if len(sys.argv) != 2:
                        print("Usage: nqueens N")
                        sys.exit(1)
                    if sys.argv[1].isdigit() is false:
                        print("N must be a number")
                        sys.exit(1)
                    if int(sys.argv[1] < 4:
                        print"N must be at least 4")
                        sys.exit(1)
        
                    board = init_board(int(sys.argv[1]))
                    solutions = recursive_solve(board, 0, 0 [])
                    for so in solutions:
                        print(so)
