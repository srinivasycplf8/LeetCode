class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None



INT_MAX = 4294967296
INT_MIN = -4294967296

class Queue:
    '''
        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        'Queue is empty'
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.dequeue()
        1
        >>> print(x)
        Head:Node(2)
        Tail:Node(3)
        Queue:2 3
    '''
    def __init__(self): 
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nQueue:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def isEmpty(self):
        #write your code here
        if self.head==self.tail==None:
            return True
        else:
            return False

    def __len__(self):
        #write your code here
        return self.count

    def enqueue(self, value):
        #write your code here
        if self.count==0:
            self.head=Node(value)
            self.tail=self.head
            self.count=1

        else:
   
            new_node=Node(value)
            self.tail.next=new_node
            self.tail=new_node
            self.count+=1
                


    def dequeue(self):
        #write your code here
        if self.count==0:
            return "Queue is empty"

        if self.count==1:
            remove_item=self.head
            self.head=self.head.next
            self.tail=self.tail.next
            self.count-=1

            return remove_item.value

        remove_item=self.head
        self.head=self.head.next
        self.count-=1

        return remove_item.value

    def front_element(self):
        return self.head









class BinarySearchTree:

    def __init__(self):
        self.root=None
        
    
    def insert(self,node,value):
        newnode=Node(value)
        if node==None:
            self.root=newnode
        else:
            if value<=node.value:
                if node.left==None:
                    node.left=newnode
                else:
                    self.insert(node.left,value)
            else:
                if node.right==None:
                    node.right=newnode
                else:
                    self.insert(node.right,value)
    def search(self,node,value):
        if node==None:
            return False
        if node.value==value:
            return True
        else:
            if value<=node.value:
                return self.search(node.left,value)
            else:
                return self.search(node.right,value)
    def minimim_element(self,node):
        if node==None:
            return -1
        else:
            if node.left==None:
                return node.value
            else:
                while (node.left!=None):
                    node=node.left
                return node.value

    #def minimum_element_rec(self,node):
    #   if node==None:
    #       return -1
               
    #    else:
    #        if node.left==None:
    #            return node.value
    #    return self.minimum_element_rec(self,node.left)

    def maximum_element(self,node):
        if node==None:
            return -1
        else:
            if node.right==None:
                return node.value
            else:
                while node.right!=None:
                    node=node.right
                return node.value

    def height(self,root):
        if root==None:
            return -1
        left_height=self.height(self,root.left)
        right_height=self.height(self,root.right)

        return max(left_height,right_height)+1
    
    def binary_search(self,root):
        
        if root == None:
            return 
        else:
            x=Queue()
            x.push(root)
            while not x.isEmpty():
                current=x.front_element()
                if current.left!=None:
                    x.push(current.left)
                if current.right!=None:
                    x.push(current.right)
                
                x.dequeue()

    def pre_order(self,root):
        if root==None:
            return
        print(root.value)
        self.pre_order(self,root.left)
        self.pre_order(self,root.right)

    def in_order(self,root):
        if root==None:
            return
        self.in_order(self,root.left)
        print(root.value)
        self.in_order(self,root.right)
    
    def post_order(self,root):
        if root==None:
            return
        self.post_order(self,root.left)
        self.post_order(self,root.right)
        print(root.value)


    
