# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        queue=[]
        queue=[root]
        total=0
        while queue:
            current=queue[0]
            if current.val>=L and current.val<=R:
                total=total+current.val
            if current.left!=None:
                queue.append(current.left)
            if current.right!=None:
                queue.append(current.right)
            queue.pop(0)
        
        return total
        