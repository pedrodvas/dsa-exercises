# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        curr = head
        size = 0
        while curr:
            curr = curr.next
            size += 1
        if size <= 1:
            return None
        if n == size:
            return head.next
        to_remove = size - n + 1
        i = 0
        curr = head
        while i != to_remove - 2:
            curr = curr.next
            i += 1
        curr.next = curr.next.next
        return head