# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def searcher(head: Optional[TreeNode]):
            if not head:
                return
            searcher(head.left)
            res.append(head.val)
            searcher(head.right)


        searcher(root)
        return res