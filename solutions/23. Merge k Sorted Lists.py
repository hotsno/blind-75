# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            merged = []
            i = 0
            while i < len(lists):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merge = self.mergeLists(l1, l2)
                merged.append(merge)
                i += 2
            lists = merged
        return lists[0] if lists else None

    def mergeLists(self, l1, l2):
        dummy = cur = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        return dummy.next

