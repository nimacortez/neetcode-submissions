# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# if current node is null, return null
# swap node's left and right pointers
# recursively call dfs on new left child
# recursively call dfs on new right child
# return current node (now inverted)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return None
        
        root.right, root.left = root.left, root.right
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        