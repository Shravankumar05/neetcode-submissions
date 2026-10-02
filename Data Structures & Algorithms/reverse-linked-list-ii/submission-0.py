# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        nodes = []
        start = head
        while head:
            nodes.append(head)
            head = head.next
        while left < right:
            tmp = nodes[left-1]
            nodes[left-1] = nodes[right-1]
            nodes[right-1] = tmp
            left += 1
            right -= 1
        
        i = 0
        while i < len(nodes):
            if i == len(nodes) - 1:
                nodes[i].next = None
                break

            nodes[i].next = nodes[i+1]
            i += 1
        
        return nodes[0]