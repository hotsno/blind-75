class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                return ["x"]
            return [str(node.val)] + dfs(node.left) + dfs(node.right)
        return ''.join(dfs(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def dfs(i):
            if data[i] == 'x':
                return (None, i)
            node = TreeNode(int(data[i]))
            node.left, i = dfs(i + 1)
            node.right, i = dfs(i + 1)
            return (node, i)
        return dfs(0)
