#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    if t==None:
        return s == 0

    s = s - t.value
    if t.left is None and t.right is None:
        return s == 0
    elif t.left is not None and t.right is not None:
        return hasPathWithGivenSum(t.left, s) or hasPathWithGivenSum(t.right,s)
    elif t.left is not None and t.right is None:
        return hasPathWithGivenSum(t.left, s)
    elif t.left is None and t.right is not None:
        return hasPathWithGivenSum(t.right,s) 


        
    
