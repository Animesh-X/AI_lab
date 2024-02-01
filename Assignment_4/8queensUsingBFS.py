import copy
from queue import Queue


def is_safe(board_status):
    length = len(board_status)
    for i in range(length):
        chkrow, chkcol = board_status[i]
        for j in range(i + 1, length):
            currow, curcol = board_status[j]
            if chkrow == currow or chkcol == curcol:
                return False
            if abs(chkrow - currow) == abs(chkcol - curcol):
                return False
    return True


def solve_using_bfs(board):
    n = len(board)
    solution = []
    q = Queue()
    for i in range(n):
        q.put([(i, 0)])
    while not q.empty():
        arrangement = q.get()
        current_length = len(arrangement)
        if current_length == n and is_safe(arrangement):
            solution.append(arrangement)
            continue
        if not is_safe(arrangement):
            continue
        last_node = arrangement[current_length - 1]
        row, col = last_node
        if col == n - 1:
            continue
        for i in range(n):
            new_arrangement = copy.deepcopy(arrangement)
            new_arrangement.append((i, col + 1))
            q.put(new_arrangement)
    return solution


def print_board(solved_board):
    n = len(solved_board)
    for i in range(n):
        for j in range(n):
            if (i, j) in solved_board:
                print("Q", end=" ")
            else:
                print("-", end=" ")
        print()

size = 8
my_board = [[0] * size for _ in range(size)]
solved_boards = solve_using_bfs(my_board)
for solved_board in solved_boards:
    print_board(solved_board)
    print()
