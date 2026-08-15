# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def aux(r, l, h):
            if r.val < l or r.val > h:
                return False

            if not r.left and not r.right: 
                return r.val > l and r.val < h

            if not r.left:
                if r.right.val <= r.val: return False
                return aux(r.right, max(r.val, l), h)
            if not r.right:
                if r.left.val >= r.val: return False
                return aux(r.left, l, min(r.val, h))
            return aux(r.left, l, min(r.val, h)) and aux(r.right, max(r.val, l), h)
            
        return aux(root, float("-inf"), float("inf"))
