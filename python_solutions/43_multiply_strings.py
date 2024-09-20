"""
https://leetcode.com/problems/multiply-strings/description/

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.



Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"


Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


def multiply(num1, num2) -> str:
    if num1 == '0' or num2 == '0':
        return '0'

    len1, len2 = len(num1), len(num2)
    result = [0] * (len1 + len2)

    # Multiply each digit and store the result in the correct position
    for i in range(len1 - 1, -1, -1):
        for j in range(len2 - 1, -1, -1):
            # Calculate product of current digits
            mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            # Position in the result array
            p1 = i + j
            p2 = i + j + 1
            # Add multiplication result to the position
            sum_carry = mul + result[p2]

            # Update result array with carry and remainder
            result[p2] = sum_carry % 10
            result[p1] += sum_carry // 10

    # Convert result array to string and remove leading zeros
    result_str = ''.join(map(str, result))
    return result_str.lstrip('0')


if __name__ == "__main__":
    n1 = "123"
    n2 = "456"
    print(multiply(n1, n2))
