INT_MAX = 4294967296
INT_MIN = -4294967296

class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

def IsBSUtil(root,min_value,max_value):
    if root==None:
        return True
    if (root.value<min_value and root.value>max_value)and(IsBSUtil(root.left,min_value,root.value))and (IsBSUtil(root.right,root.value,max_value)):
        return True
    else:
        return False

def IsBinarySearchTree(root):
    return IsBSUtil(root,INT_MAX,INT_MIN)

def calculateSum(self, temp):  
    total = sumRight = sumLeft = 0;  
        
    #Check whether tree is empty  
    if(self.root == None):  
        return 0;  
    else:  
        #Calculate the sum of nodes present in left subtree  
        if(temp.left != None):  
            sumLeft = self.calculateSum(temp.left);  
            
        #Calculate the sum of nodes present in right subtree  
        if(temp.right != None):  
            sumRight = self.calculateSum(temp.right);  
            
        #Calculate the sum of all nodes by adding sumLeft, sumRight and root node's data  
        total = temp.value + sumLeft + sumRight;   
    return total;      

def maxSumBST(self, root) :
    if IsBinarySearchTree(root):
        #Find the Max Sum

        return calculateSum(self,root)
    

