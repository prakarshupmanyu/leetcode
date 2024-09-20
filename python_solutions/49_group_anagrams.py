"""
https://leetcode.com/problems/group-anagrams/description/

Given an array of strings strs, group the
anagrams
 together. You can return the answer in any order.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]



Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    result = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        result[sorted_word].append(word)
    return list(result.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(strs))
