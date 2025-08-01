from typing import List, Tuple, Set, Optional


# We define the types of a partial picture and a constraint (for type checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]


def max_seen_cells(picture: Picture, row: int, col: int) -> int:
    if picture[row][col] == 0:
        return 0
    counter = 1
    for i in range(col+1, len(picture[0])):
        if picture[row][i] == 0:
            break
        counter += 1
    for i in range(col-1, -1,-1):
        if picture[row][i] == 0:
            break
        counter += 1
    for i in range(row+1,len(picture)):
        if picture[i][col] == 0:
            break
        counter+=1
    for i in range(row-1,-1,-1):
        if picture[i][col] == 0:
            break
        counter += 1
    return counter


def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    picture2 = [[0 if picture[i][j] == -1 else picture[i][j] for j in range(len(picture[i]))] for i in range(len(picture))]
    return max_seen_cells(picture2, row, col)


def check_constraints(picture: Picture, constraints_set: Set[Constraint]) -> int:
    result = 1
    for tup in constraints_set:
        min_cells = min_seen_cells(picture, tup[0], tup[1])
        max_cells = max_seen_cells(picture, tup[0], tup[1])
        seen = tup[2]
        if min_cells == max_cells == seen:
            pass
        elif min_cells<= seen <= max_cells:
            result = 2
        else:
            return 0
    return result


def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[Picture]:
    board = build_board(n, m)
    solve_puzzle_helper(constraints_set, 0, 0, board)
    if check_bool(board):
        return board


def build_board(r, c):
    board = []
    for _ in range(r):
        row = []
        for _ in range(c):
            row.append(-1)
        board.append(row)
    return board


def check_bool(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == -1:
                return False
        return True


def find_constraints(cons, r, c):
    lst = []
    for i in cons:
        if i[0] == r or i[1] == c:
            lst.append(i)
    return set(lst)


def solve_puzzle_helper(cons, r, c, board):
    if r > len(board) - 1:
        return board
    if c == len(board[0]) - 1:
        new_c = 0
        new_r = r + 1
    else:
        new_r = r
        new_c = c + 1
    board[r][c] = 0
    constraints = find_constraints(cons, r, c)
    if check_constraints(board, constraints) != 0:
        if solve_puzzle_helper(cons, new_r, new_c, board):
            return board
    board[r][c] = 1
    if check_constraints(board, constraints) != 0:
        if solve_puzzle_helper(cons, new_r, new_c, board):
            return board
    board[r][c] = -1


def how_many_solutions_helper(cons, r, c, board, n):
    if r > len(board) - 1:
        n += 1
        return n
    if c == len(board[0]) - 1:
        new_c = 0
        new_r = r + 1
    else:
        new_r = r
        new_c = c + 1
    board[r][c] = 0
    constraints = find_constraints(cons, r, c)
    if check_constraints(board, constraints) != 0:
        n = how_many_solutions_helper(cons, new_r, new_c, board, n)
    board[r][c] = 1
    if check_constraints(board, constraints) != 0:
        n = how_many_solutions_helper(cons, new_r, new_c, board, n)
    board[r][c] = -1
    return n


def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int) -> int:
    board = build_board(n, m)
    n = how_many_solutions_helper(constraints_set, 0, 0, board, 0)
    return n


def generate_puzzle(picture: Picture) -> Set[Constraint]:
    return {(0, 0, 1)}

