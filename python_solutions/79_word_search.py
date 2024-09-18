"""
https://leetcode.com/problems/word-search/description/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
"""


def search_word(board, word):
    r = len(board)
    c = len(board[0])

    def look_further(k, i, j):
        if k == len(word):
            return True
        if i >= r or j >= c or i < 0 or j < 0 or word[k] != board[i][j]:
            return False
        temp = board[i][j]
        board[i][j] = ''
        if (look_further(k+1, i+1, j) or   #down
                look_further(k+1, i, j+1) or   #right
                look_further(k+1, i-1, j) or   #up
                look_further(k+1, i, j-1)):     #left
            return True

        board[i][j] = temp
        return False

    for row in range(r):
        for j in range(c):
            if look_further(0, row, j):
                return True
    return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"

    board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    word = "ABCESEEEFS"
    print(search_word(board, word))
