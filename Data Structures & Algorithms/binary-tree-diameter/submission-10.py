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
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0
        
            left = dfs(curr.left)
            right = dfs(curr.right)
            
            self.res = max(self.res, left + right)
            return 1 + max(left, right) 
        
        dfs(root)
        return self.res