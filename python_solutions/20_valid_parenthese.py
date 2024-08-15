"""
https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


def is_valid(s: str) -> bool:
    opening_brackets = ['[', '{', '(']
    close_open_map = {']': '[', '}': '{', ')': '('}
    n = len(s)
    i = 0
    opened_stack = []
    opened_stack_top = -1
    while i < n:
        ch = s[i]
        if ch in opening_brackets:
            opened_stack.append(ch)
            opened_stack_top += 1
        else:   # in case of closing brace
            if opened_stack_top < 0:
                return False
            last_open_brace = opened_stack.pop(opened_stack_top)
            if last_open_brace != close_open_map[ch]:
                return False
            opened_stack_top -= 1
        i += 1

    if opened_stack_top > -1:
        return False

    return True


if __name__ == "__main__":
    print(is_valid("([)]"))
