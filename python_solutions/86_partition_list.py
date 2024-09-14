"""
https://leetcode.com/problems/partition-list/description/

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater 
than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

<image_inserted> 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition_list(list_head: ListNode, x: int):
    curr_node = list_head
    left = None
    right = list_head
    right_start = None
    while curr_node is not None:
        if curr_node.val < x:
            if not left:
                left = curr_node
                list_head = curr_node
            else:
                left.next = curr_node
                left = curr_node
        else:
            if not right_start:
                right_start = curr_node
            else:
                right.next = curr_node
            right = curr_node
        curr_node = curr_node.next
    if left and right_start:
        right.next = None
        left.next = right_start
    return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)
    head = partition_list(head, 3)
    curr = head
    while curr:
        print(curr.val, "->")
        curr = curr.next
