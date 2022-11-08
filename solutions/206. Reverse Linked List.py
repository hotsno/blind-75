# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur, next = None, head, head.next
        while next:
            cur.next = prev
            temp = next.next
            next.next = cur
            prev = cur
            cur = next
            next = temp
        return cur

# Need to understand better
