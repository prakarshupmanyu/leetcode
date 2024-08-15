"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result: ListNode = ListNode()
    curr_node = result

    carry = 0
    while l1 is not None and l2 is not None:
        node_sum = l1.val + l2.val + carry
        curr_node.val = node_sum % 10
        curr_node.next = ListNode()
        prev = curr_node
        curr_node = curr_node.next
        l1 = l1.next
        l2 = l2.next
        carry = 1 if node_sum > 9 else 0

    l: ListNode = l1 if l1 else l2

    while l is not None:
        node_sum = l.val + carry
        carry = 1 if node_sum > 9 else 0
        curr_node.val = node_sum % 10
        curr_node.next = ListNode()
        prev = curr_node
        curr_node = curr_node.next
        l: ListNode = l.next

    if carry > 0:
        curr_node.val = carry
        prev = curr_node
    prev.next = None
    return result


if __name__ == "__main__":
    l11 = ListNode(2)
    l12 = ListNode(3)
    l11.next = l12
    l21 = ListNode(1)
    l22 = ListNode(2)
    l21.next = l22
    lsum = addTwoNumbers(l11, l21)
    curr = lsum
    while curr:
        print(curr.val, "->")
        curr = curr.next
