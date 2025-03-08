def solveNQueens(N):
    def backtrack(row, cols, diag1, diag2, board):
        if row == N:
            result.append(["".join(r) for r in board])  
            return

        for col in range(N):
            if (cols & (1 << col)) or (diag1 & (1 << (row - col + N - 1))) or (diag2 & (1 << (row + col))):
                continue  
            
            board[row][col] = 'Q'
            backtrack(row + 1, cols | (1 << col), diag1 | (1 << (row - col + N - 1)), diag2 | (1 << (row + col)), board)
            board[row][col] = '.'
    
    result = []
    empty_board = [["."] * N for _ in range(N)]
    backtrack(0, 0, 0, 0, empty_board)
    return result

# Usage
N = 4
solutions = solveNQueens(N)
for sol in solutions:
    for row in sol:
        print(row)
    print()
