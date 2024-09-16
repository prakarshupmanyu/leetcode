"""
https://leetcode.com/problems/pascals-triangle-ii/description/

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]


Constraints:

0 <= rowIndex <= 33
"""


def pascal_triangle(row_index):
    dp = [0] * (row_index + 1)
    dp[0] = 1
    for i in range(1, row_index + 1):
        for j in range(i, 0, -1):
            dp[j] = dp[j-1] + dp[j]
    return dp


if __name__ == "__main__":
    row_index = 5
    print(pascal_triangle(row_index))
