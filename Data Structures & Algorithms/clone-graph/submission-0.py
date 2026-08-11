"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        seen = {}

        def aux(n):
            if not n or n.val in seen:
                return
            seen[n.val] = Node(n.val, [])
            for neighbor in n.neighbors:
                aux(neighbor)
                seen[n.val].neighbors.append(seen[neighbor.val])
        if not node:
            return None
        aux(node)
        return seen[1]
