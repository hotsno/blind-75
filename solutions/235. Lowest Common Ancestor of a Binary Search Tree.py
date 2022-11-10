# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        smaller, bigger = p, q
        if q.val < p.val:
            smaller, bigger = q, p
        while True:
            if smaller.val <= root.val <= bigger.val:
                return root
            if root.val > smaller.val:
                root = root.left
            else:
                root = root.right
