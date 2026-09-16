# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# returns [isBalanced, height]
# for each node: curisvely get results from left and right children
# left subtree and right subtree must be balanced, height diff <= 1
# height of current node = 1 + max(leftHeight, rightHeight)
# run dfs on the root and return isBalanced

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root): 
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]



