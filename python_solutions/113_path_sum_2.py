"""
https://leetcode.com/problems/path-sum-ii/description/

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.



Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum2(target, root):
    if not root:
        return []

    result = []

    def find_path(target, path, root):
        if not root:
            return []
        if not root.left and not root.right:
            if target == root.val:
                result.append(path + [root.val])
        find_path(target - root.val, path + [root.val], root.left)
        find_path(target - root.val, path + [root.val], root.right)
    find_path(target, [], root)
    return result


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(8)
    root.right.left = TreeNode(6)
    root.right.left.right = TreeNode(7)
    root.right.right = TreeNode(9)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.left = TreeNode(6)
    root2.right.right = TreeNode(7)

    root3 = TreeNode(5)
    root3.left = TreeNode(4)
    root3.right = TreeNode(6)
    root3.right.left = TreeNode(3)
    root3.right.right = TreeNode(7)

    root4 = TreeNode(5)
    root4.left = TreeNode(4)
    root4.left.left = TreeNode(11)
    root4.left.left.left = TreeNode(7)
    root4.left.left.right = TreeNode(2)
    root4.right = TreeNode(8)
    root4.right.left = TreeNode(13)
    root4.right.right = TreeNode(4)
    root4.right.right.left = TreeNode(5)
    root4.right.right.right = TreeNode(1)
    print(path_sum2(14, root))    # true
    print(path_sum2(8, root2))  # true
    print(path_sum2(3, root3))   # false
    print(path_sum2(22, root4))  # true
