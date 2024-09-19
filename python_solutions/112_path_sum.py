"""
https://leetcode.com/problems/path-sum/description/

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.



Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.


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


def path_sum(target, root) -> bool:
    if not root:
        return False

    if not root.left and not root.right:
        if target == root.val:
            return True
        return False

    return path_sum(target - root.val, root.left) or path_sum(target - root.val, root.right)


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
    root4.right.right.right = TreeNode(1)
    print(path_sum(14, root))    # true
    print(path_sum(8, root2))  # true
    print(path_sum(3, root3))   # false
    print(path_sum(22, root4))  # true
