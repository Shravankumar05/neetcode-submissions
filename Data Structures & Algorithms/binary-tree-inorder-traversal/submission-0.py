# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left, root, right
        res = []
        if not root:
            return res

        def dive(node: Optional[TreeNode]):
            if node.left:
                dive(node.left)
            res.append(node.val)
            if node.right:
                dive(node.right)
        
        dive(root)
        return res