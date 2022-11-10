# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return 0
        left, right = self.helper(root.left), self.helper(root.right)
        path_max = max(root.val, root.val + left, root.val + right)
        self.res = max(self.res, path_max, root.val + left + right)
        return path_max
