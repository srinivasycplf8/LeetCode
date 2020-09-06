# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root==None:
            return True
        def valid(root,mini,maxi):
            
            if root==None:
                return True
            
            elif (mini!=None and mini<=root.val) or (maxi!=None and maxi>=root.val):
                return False
              
            else:
                return valid(root.left,root.val,maxi) and valid(root.right,mini,root.val)
                




        return valid(root,None,None)
        