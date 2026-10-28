# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isequiv(head1: Optional[TreeNode], head2: Optional[TreeNode]) -> bool:
            if not head1 and not head2:
                return True
            if not head1 or not head2:
                return False
            if head1.val != head2.val:
                return False
            
            return isequiv(head1.left, head2.left) and isequiv(head1.right, head2.right)
        
        def whereroot(head: Optional[TreeNode]) -> bool:
            if not head:
                return False
            if isequiv(head, subRoot):
                return True
            return whereroot(head.left) or whereroot(head.right)
        
        if not subRoot:
            return True

        return whereroot(root)