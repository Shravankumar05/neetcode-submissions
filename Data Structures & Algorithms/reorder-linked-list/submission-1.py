# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        order = []
        start = head

        while head:
            order.append(head)
            head = head.next
        
        i = 0
        head = start
        while i < len(order) // 2:
            head.next = order[len(order)-1-i]
            head = head.next
            head.next = order[i+1]
            head = head.next
            i += 1

        head.next = None
        return