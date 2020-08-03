class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        

                          
class OrderedLinkedList:  
    '''
        >>> x=OrderedLinkedList()
        >>> x.pop()
        'List is empty'
        >>> x.add(-6)
        >>> x.add(8)
        >>> x.add(3)
        >>> x.add(7)
        >>> print(x)
        Head:Node(8)
        Tail:Node(-6)
        List:8 7 3 -6
        >>> len(x)
        4
        >>> x.pop()
        -6
        >>> print(x)
        Head:Node(8)
        Tail:Node(3)
        List:8 7 3
    '''
    def __init__(self):
    	#You can add a count attribute for len
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=(' '.join(out))
       
        return ('Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def add(self, value):
        #write your code here
        newnode=Node(value)
        if self.isEmpty():
            self.head=newnode
            self.tail=newnode
        elif (value>=self.head.value):
            newnode.next=self.head
            self.head=newnode
        elif self.head.value>value>self.tail.value:
            current=self.head
            previous=None
            while current.value>value:
                previous=current
                current=current.next
            previous.next=newnode
            newnode.next=current
        else :
            current=self.head
            previous=None
            while (current is not None and current.value>value):
                previous=current
                current=current.next
            previous.next=newnode
            newnode.next=current
            if current is None:
                self.tail=newnode
        self.count+=1
            

    def pop(self):
    #write your code here
        if self.isEmpty():
            return "List is empty"
        end=self.tail
        begin=self.head
        if begin==end:
            self.head=self.tail=None
            return end.value
        while begin.next is not end:
            begin=begin.next
        begin.next=None
        self.tail=begin
        self.count-=1

        return end.value
        

    def isEmpty(self):
        #write your code here
        return self.head==None
            
        

    def __len__(self):
        #write your code here
        return self.count
