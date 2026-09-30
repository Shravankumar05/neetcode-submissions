# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        nodes = []
        
        while head:
            nodes.append(head)
            head = head.next
        
        target = len(nodes)-n
        if target == 0:
            return start.next
        i = 1
        head = start

        while head:
            if i == target:
                head.next = head.next.next
                return start
            else:
                head = head.next
                i += 1
        
        return start