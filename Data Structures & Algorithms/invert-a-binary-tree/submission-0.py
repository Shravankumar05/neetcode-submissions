# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inverter(head: Optional[TreeNode]):
            if not head:
                return
            tmp = head.left
            head.left = head.right
            head.right = tmp
            inverter(head.left)
            inverter(head.right)
            return
        inverter(root)
        return root