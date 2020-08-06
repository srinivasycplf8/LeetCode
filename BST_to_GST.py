def bstToGst(self, root: TreeNode) -> TreeNode:
    self.total = 0
    self.gst(root)
    return root
    
def gst(self,node):
    if node == None:
        return 0
    self.gst(node.right)
    self.total += node.val
    node.val = self.total
    self.gst(node.left)
    
