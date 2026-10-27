# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []

        x = l1
        while x:
            num1.append(x.val)
            x = x.next
        
        x = l2
        while x:
            num2.append(x.val)
            x = x.next
        
        val1 = 0
        val2 = 0
        i = 0
        while i < len(num1):
            val1 += (num1[i] * pow(10, i))
            i += 1
        i = 0
        while i < len(num2):
            val2 += (num2[i] * pow(10, i))
            i += 1
        total = val1 + val2
        total_str = str(total)[::-1]
        print(total_str)
        head = ListNode()
        dummy = head

        for digit in total_str:
            next_node = ListNode()
            next_node.val = int(digit)
            head.next = next_node
            head = head.next
        
        return dummy.next