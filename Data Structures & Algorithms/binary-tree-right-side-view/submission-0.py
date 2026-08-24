# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        toVisit = deque([root])
        res = []

        while toVisit:
            n = len(toVisit)
            for i in range(n):
                curr = toVisit.popleft()
                if i == n - 1: res.append(curr.val)
                if curr.left: toVisit.append(curr.left)
                if curr.right: toVisit.append(curr.right)

        return res