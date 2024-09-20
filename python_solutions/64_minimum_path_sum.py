"""
https://leetcode.com/problems/minimum-path-sum/description/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""


def minimum_path(grid) -> int:
    m = len(grid)
    n = len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if i > 0 and j > 0:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
            elif i > 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = dp[i][j-1] + grid[i][j]
    return dp[m-1][n-1]


if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(minimum_path(grid))
    grid = [[1, 2, 3], [4, 5, 6]]
    print(minimum_path(grid))