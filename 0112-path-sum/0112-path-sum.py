# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,s,target):
            if not node:
                return False
            s += node.val
            if s == target and not node.left and not node.right:
                return True
            r = dfs(node.right,s,target) or dfs(node.left,s,target)
            return r
        return dfs(root,0,targetSum)
            
            