"""
https://leetcode.com/problems/first-missing-positive/description/

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""


def first_positive(nums) -> int:
    n = len(nums)
    if n == 0 or (n == 1 and nums[0] != 1):
        return 1
    if n == 1 and nums[0] == 1:
        return 2
    for i in range(n):
        while 0 <= nums[i] < n and i != nums[i]:
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    for i in range(1, n):
        if nums[i] < 0:
            return i
        if i != nums[i]:
            return i
    return n


def first_positive_optimal(nums) -> int:
    nums = [n for n in nums if n > 0]

    for n in nums:
        idx = abs(n) - 1
        if idx < len(nums) and nums[idx] > 0:
            nums[idx] *= -1

    for i in range(len(nums)):
        if nums[i] > 0:
            return i + 1

    return len(nums) + 1


if __name__ == "__main__":
    nums = [1, 2, 0]
    print(first_positive(nums))
    print(first_positive_optimal(nums))
    nums = [7,8,9,11,12]
    print(first_positive(nums))
    print(first_positive_optimal(nums))
    nums = [3, 4, -1, 1]
    print(first_positive(nums))
    print(first_positive_optimal(nums))
