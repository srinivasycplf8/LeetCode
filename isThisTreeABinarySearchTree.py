
INT_MAX = 4294967296
INT_MIN = -4294967296

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

def IsBSUtil(root,min_value,max_value):
    if root==None:
        return True
    if (root.value<min_value and root.value>max_value)and(IsBSUtil(root.left,min_value,root.value))and (IsBSUtil(root.right,root.value,max_value)):
        return True
    else:
        return False

def IsBinarySearchTree(root):
    return IsBSUtil(root,INT_MAX,INT_MIN)