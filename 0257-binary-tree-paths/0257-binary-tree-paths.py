# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node,p,res):
            if not node:
                return 
            p += str(node.val)
            if not node.left and not node.right:
                res.append(p)
            else:
                dfs(node.left,p + '->',res)
                dfs(node.right,p+ '->',res)
        res = []
        dfs(root,'',res)
        return res