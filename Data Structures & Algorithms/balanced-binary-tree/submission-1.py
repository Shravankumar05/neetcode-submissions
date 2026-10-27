# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def depth(head: Optiona[TreeNode]) -> int:
            if not head:
                return 0
            return 1 + max(depth(head.left), depth(head.right))
        
        if not root:
            return True

        L = depth(root.left)
        R = depth(root.right)
        diff = abs(L-R)
        if diff > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)