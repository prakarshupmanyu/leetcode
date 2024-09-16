"""
https://leetcode.com/problems/pascals-triangle/description/

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30

"""
from typing import List


def pascal_triangle(num_rows: int) -> List[List[int]]:
    output = []
    for i in range(num_rows):
        output.append([1]*(i+1))
        for j in range(1, i):
            output[i][j] = output[i-1][j-1] + output[i-1][j]
    return output


if __name__ == "__main__":
    num_rows = 5
    print(pascal_triangle(num_rows))
