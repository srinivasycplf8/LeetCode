# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        queue=[root]
        while queue:
            current=queue.pop(0)
            if current.left!=None :
                if current.left.val==current.val:
                    queue.append(current.left)
                else:
                    return False
            
            if current.right!=None:
                if current.right.val==current.val:
                    queue.append(current.right)
            
                else:
                    return False
        
        return True