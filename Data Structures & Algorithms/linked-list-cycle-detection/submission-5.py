# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        c1 = head.next
        if not c1:
            return False
        c2 = head.next.next

        while c1 and c2:
            if c1 == c2:
                return True
            else:
                c1 = c1.next
                if not c2.next:
                    return False
                c2 = c2.next.next
        
        return False