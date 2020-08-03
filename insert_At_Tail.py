class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None

def insertNodeAtTail(head,data):
    newnode=Node(data)
    if head is  None:
        return newnode
    current=head
    while current.next is not None :
        current=current.next
    current.next=newnode

    return head

    