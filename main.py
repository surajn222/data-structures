# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
#
# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells, (if you can connect the region with 'X' cells) and (none of the region cells are on the edge of the board).
# A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.
#
# Example 1:
#
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
#
# Example 2:
#
# Input: board = [["X"]]
#
# Output: [["X"]]
#
# Constraints:
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
# bfs()
# 	if on the edge, skip
# 	else
# 		check for surrounding cells
# 		if 0 in surrounding cells, call same funciton bfs
from collections import deque
def main():
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    bfs(board)


def bfs(matrix, i, j):
    queue = deque(matrix[0][0])

    while queue:
        queue.popleft()
        # check for edge condition

        # without edge condition
        queue.append(matrix, i+1, j)
        queue.append(matrix, i + 1, j+1)
        queue.append(matrix, i, j+1)
        queue.append(matrix, i + 1, j)





