# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        d = {}
        arr = []

        while curr:
            arr.append(curr)
            d[curr] = prev
            prev = curr
            curr = curr.next

        rem = arr[len(arr)-n]

        if d[rem]:
            if d[rem].next:
                d[rem].next = d[rem].next.next
            else:
                d[rem].next = None
        else:
            head = rem.next
        return head
        

            
            