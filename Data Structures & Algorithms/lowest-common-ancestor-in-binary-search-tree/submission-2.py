# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
# if p and q are both greater than current node, move right
# if p and q are smaller, move left
# if they split, current node is LCA

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        while cur: 
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else: 
                return cur