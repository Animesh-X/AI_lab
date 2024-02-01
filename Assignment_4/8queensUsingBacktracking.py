def is_safe(board, col, row, n):
    # Checking the row to see if there is any queen present
    for i in range(0, col):
        if board[row][i] == 1:
            return False
    nrow = row
    ncol = col
    for i in range(0, col):
        nrow -= 1
        ncol -= 1
        if 0 <= nrow < n and 0 <= ncol < n:
            if board[nrow][ncol] == 1:
                return False
    nrow = row
    ncol = col
    for i in range(0, col):
        nrow += 1
        ncol -= 1
        if 0 <= nrow < n and 0 <= ncol < n:
            if board[nrow][ncol] == 1:
                return False
    return True


def solve_using_dfs(board, col):
    n = len(board)
    if col == n:
        return True

    for i in range(n):
        if is_safe(board, col, i, n):
            board[i][col] = 1
            if solve_using_dfs(board, col + 1):
                return True
            board[i][col] = 0
    return False


my_list = [[0]*8 for _ in range(8)]
solve_using_dfs(my_list,0)
for row in my_list:
    print(row)