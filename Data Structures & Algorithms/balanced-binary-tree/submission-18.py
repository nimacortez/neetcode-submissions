# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# self.banaced = True, assume balanced unless proven otherwise
# if node is empty, return 0 
# recursively call left childs, then right
# subtract two heights, take abs so direction doesnt matter
# if gap more than 1, self.balanced = False
# return max of left and right
# call dfs to run whole thing 

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            if (abs(left - right) > 1):
                self.balanced = False
            return max(left, right) + 1
        
        dfs(root)
        return self.balanced

