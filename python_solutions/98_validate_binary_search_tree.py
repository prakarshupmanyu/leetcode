"""
https://leetcode.com/problems/validate-binary-search-tree/description/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode) -> bool:

    def valid(root, minimum, maximum) -> bool:
        if not root:
            return True
        if maximum <= root.val or root.val <= minimum:
            return False
        return valid(root.left, minimum, root.val) and valid(root.right, root.val, maximum)
    return valid(root, float('-inf'), float('inf'))


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
    print(is_valid_bst(root))
    print(is_valid_bst(root2))
    print(is_valid_bst(root3))
