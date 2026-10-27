# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def deeper(head: Optional[TreeNode], curr: int) -> int:
            if not head:
                return curr
            curr += 1
            return max(deeper(head.left, curr), deeper(head.right, curr))
        
        return deeper(root, 0)