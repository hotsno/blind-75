"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cache = {}
        def dfs(node):
            if node in cache:
                return cache[node]
            cache[node] = Node(node.val)
            for neighbor in node.neighbors:
                cache[node].neighbors.append(dfs(neighbor))
            return cache[node]
        return dfs(node) if node else None
