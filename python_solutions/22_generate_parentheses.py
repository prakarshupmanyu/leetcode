"""
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""
from typing import List


def generate_parentheses(n):
    """
    :type n: int
    :rtype: List[str]
    """
    output = []

    def create(openP, closeP, s):
        if openP + closeP == 2 * n:
            output.append(s)
            return

        if openP < n:
            create(openP + 1, closeP, s + '(')

        if closeP < openP:
            create(openP, closeP + 1, s + ')')

    create(0, 0, '')
    return output


if __name__ == "__main__":
    print(generate_parentheses(3))
