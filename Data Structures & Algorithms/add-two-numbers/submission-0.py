# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        val1 = []
        while head:
            val1.append(head.val)
            head = head.next
        
        head = l2
        val2 = []
        while head:
            val2.append(head.val)
            head = head.next
        
        x1 = 0
        i = 0
        while i < len(val1):
            x1 += val1[i] * pow(10, i)
            i += 1
        
        x2 = 0
        i = 0
        while i < len(val2):
            x2 += val2[i] * pow(10, i)
            i += 1
        
        total = x1 + x2
        total = str(total)
        total = total[::-1]
        start = ListNode()
        head = start
        i = 0
        while i < len(total):
            head.val = int(total[i])
            if i < len(total) - 1:
                head.next = ListNode()
                head = head.next

            i += 1

        return start