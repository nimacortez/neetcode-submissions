# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# if subroot is empty -> return true (empty tree always a subtree)
# if root is empty but subroot isnt, return false
# if sameTree(root, subRoot) is true, return true
# recursively check isSubtree(root.left, subRoot)
# recursively check isSubtree(root.right, subRoot)
# return true if either side returns true

# sameTree(root1,root2) 
# if both sides are null, return true
# if only one side is null, return false
# if values diff, return false
# recursively check left and right children

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)) 

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: 
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
            return False




        