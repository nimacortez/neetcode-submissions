# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# use dfs to compute height of every subtree
# for each node, recursively get left height
# get right height
# diameter through this node = left + right
# update global answer with the diameter
# height returned to parent = 1 + max(left, right)
# after dfs finishes, global answer contains the diameter

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return res



