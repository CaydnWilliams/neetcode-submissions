# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]) :
            if root == None :
                return 0

            leftDepth = dfs(root.left) 
            rightDepth = dfs(root.right) 

            if leftDepth < 0 or rightDepth < 0 :
                return -1
            if abs(leftDepth - rightDepth) > 1 :
                return -1
            return 1 + max(leftDepth, rightDepth)
        return dfs(root) >= 0