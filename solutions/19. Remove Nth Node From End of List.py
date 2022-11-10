# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head_start = head
        for i in range(n - 1):
            head_start = head_start.next
        dummy = prev = ListNode(next=head)
        while head_start.next:
            prev = cur
            cur = cur.next
            head_start = head_start.next
        prev.next = cur.next
        return dummy.next
