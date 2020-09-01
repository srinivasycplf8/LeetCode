# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result=[]
        if root==None:
            return result
        self.dfs(root,"",result)
        
        return result
    
    def dfs(self,node:TreeNode,path,result):
        path+=str(node.val)
        if node.left==None and node.right==None:
            result.append(path)
            return result
        if node.left!=None:
            self.dfs(node.left,path+"->",result)
        if node.right!=None:
            self.dfs(node.right,path+"->",result)

"""Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3"""