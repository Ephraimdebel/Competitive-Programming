# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(node,count):
            if node:
                count = count +1
                res.append(count)
                dfs(node.left,count)
                dfs(node.right,count)
            return res
        return max(dfs(root,0)) if root else 0
