# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# if root is null, return 0
# recursively comput leftDepth = maxDepth(root.left)
# rightDepth = maxDepth(root.Right)
# 1 + max(leftDepth, rightDepth)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))