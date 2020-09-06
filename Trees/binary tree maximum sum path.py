# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result= -100000

    def maxPathSum(self, root: TreeNode) -> int:
        def maxResult(root,result=self.result):
            if root==None:
                return 0
            left = maxResult(root.left,self.result)
            right = maxResult(root.right,self.result)
            

            ms = max(max(left,right)+root.val,root.val)

            m2l = max(ms,left+right+root.val)
            
            self.result=max(m2l,self.result)
    
        
            return ms #the reason we are returing only ms because m2l and result depnds on it
    
        maxResult(root,self.result)
        return self.result
        