# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        coll = []
        def inorder(node):
            if node:
                inorder(node.left)
                coll.append(node)
                inorder(node.right)
        inorder(root)

        def divide(nums,l,r):
            if l > r:
                return None
            if l == r:
                nums[l].left = None
                nums[l].right = None
                return nums[l]
            m = (l+r)//2
            
            node = nums[m]
            node.left = divide(nums,l,m-1)
            node.right = divide(nums,m+1,r)

            return node
        return divide(coll,0,len(coll)-1)

        # print(coll)