# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(p,q):
            if not p:
                return q

            if not q:
                return p
   
            node = TreeNode(p.val + q.val)
            node.left = dfs(p.left,q.left)
            node.right = dfs(p.right,q.right)
            return node
        
        return dfs(root1,root2)