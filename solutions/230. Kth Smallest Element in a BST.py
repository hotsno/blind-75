# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    k = 0
    res = None
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.helper(root)
        return self.res

    def helper(self, cur):
        if self.res is not None:
            return
        if cur.left:
            self.helper(cur.left)
        self.count += 1
        if self.count == self.k:
            self.res = cur.val
        if cur.right:
            self.helper(cur.right)
