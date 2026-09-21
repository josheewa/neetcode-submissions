# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        q = deque([root])
        res = ""

        while q:
            curr = q.popleft()
            if not curr:
                res += ' x'
                continue
            res += ' '+str(curr.val)
            q.append(curr.left)
            q.append(curr.right)
        print(res)
        return res


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        data = data.split()
        root = TreeNode(int(data[0]), None, None)
        q = deque([root])
        i = 0

        while q and i < len(data):
            curr = q.popleft()
            if i+1 < len(data) and data[i+1] != 'x':
                curr.left = TreeNode(int(data[i+1]), None, None)
                q.append(curr.left)
            if i+2 < len(data) and data[i+2] != 'x':
                curr.right = TreeNode(int(data[i+2]), None, None)
                q.append(curr.right)
            i += 2
        return root