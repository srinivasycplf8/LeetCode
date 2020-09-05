# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
 
        
    def countNodes(self, root: TreeNode) -> int:
        if root==None:
            return 0
        l=root.left
        r=root.right
        left_level=1
        while l:
            l=l.left
            left_level+=1
        right_level=1
        while r:
            r=r.right
            right_level+=1
        if left_level==right_level:
            return 2**left_level - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        