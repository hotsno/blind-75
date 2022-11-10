# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, None, None)
    def helper(self, root, min, max):
        if not root:
            return True
        if (min is not None and root.val <= min) or (max is not None and root.val >= max):
            return False
        return self.helper(root.left, min, root.val) and self.helper(root.right, root.val, max)

