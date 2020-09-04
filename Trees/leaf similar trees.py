# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.queue1=[]
        self.queue2=[]
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def isleaf(root,queue):
            if root:
                if root.left==None and root.right==None:
                    queue.append(root.val)
                else:


                    isleaf(root.left,queue)
                    isleaf(root.right,queue)

                
        isleaf(root1,self.queue1)
        isleaf(root2,self.queue2)
        
        print(self.queue1)
        print(self.queue2)
        
        return self.queue1==self.queue2 
        