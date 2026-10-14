# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        arr = []
        for l in lists:
            while l:
                arr.append(l.val)
                l = l.next
        if not arr:
            return None
        arr.sort()
        
        root = ListNode(arr[0])
        curr = root
        for x in arr[1:]:
            curr.next = ListNode(x)
            curr = curr.next

        return root