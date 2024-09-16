"""
https://leetcode.com/problems/valid-palindrome/description/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


def is_valid_palindrome(string: str) -> bool:
    i = 0
    j = len(string) - 1
    string = string.lower()
    while i < len(string) and j >= 0 and i <= j:
        ch = string[i]
        while not ch.isalnum() and i + 1 < len(string):
            i += 1
            ch = string[i]
        ch2 = string[j]
        while not ch2.isalnum() and j - 1 >= 0:
            j -= 1
            ch2 = string[j]
        if not ch == ch2 and i <= j:
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    s = ".,"
    s = " apG0i4maAs::sA0m4i0Gp0"
    print(is_valid_palindrome(s))
