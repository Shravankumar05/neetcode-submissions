# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        x = head
        if not head:
            return None
        
        while x:
            count += 1
            x = x.next
        
        target = count - n
        if target == 0:
            return head.next
        x = head
        i = 0

        while x:
            if i == target-1:
                x.next = x.next.next
                break
            x = x.next
            i += 1
        return head