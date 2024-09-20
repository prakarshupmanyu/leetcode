"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.



Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_duplicates(head: ListNode) -> ListNode:
    if not head:
        return head

    curr = head
    prev = None
    while curr:
        if not prev:
            prev = curr
        else:
            if prev.val != curr.val:
                prev.next = curr
                prev = curr
        curr = curr.next
    if prev:
        prev.next = None
    return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    remove_duplicates(head)
    curr = head
    while curr:
        print(curr.val, "->")
        curr = curr.next
