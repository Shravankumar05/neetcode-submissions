# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        x = []
        c = head

        while c:
            x.append(c)
            c = c.next
        
        left = 1
        right = len(x)-1
        
        while left <= right:
            head.next = x[right]
            head = head.next
            right -= 1

            if left <= right:
                head.next = x[left]
                head = head.next
                left += 1
        
        head.next = None
        return