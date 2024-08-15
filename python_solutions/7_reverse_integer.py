"""

https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1
"""


def reverse(x: int) -> int:
    n: int = 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    while x / 10 > 0:
        n = 10 * n + (x % 10)
        x = int(x / 10)
    return n * sign if -2147483648 <= n * sign <= 2147483647 else 0


if __name__ == "__main__":
    print(reverse(123))
