# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.ans=0
    
    def dfs(self,root,val):
        if root==None:
            return
        val=val*2
        val=val+root.val
        if root.left==None and root.right==None:
            self.ans+=val
            return
        
        self.dfs(root.left,val)
        self.dfs(root.right,val)
        
  
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.dfs(root,0)
        return self.ans