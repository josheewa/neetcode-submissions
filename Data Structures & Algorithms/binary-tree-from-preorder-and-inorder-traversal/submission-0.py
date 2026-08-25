# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        m = {x: i for i, x in enumerate(inorder)}
        idx = 0

        def aux(l, r):
            nonlocal idx
            if l > r: return None

            val = preorder[idx]
            idx += 1

            root = TreeNode(val)
            mid = m[val]

            root.left = aux(l, mid-1)
            root.right = aux(mid+1, r)

            return root
        return aux(0, len(preorder)-1)