
class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None

def insertNodeAtHead(head,data):
    newnode=Node(data)
    if head is  None:
        return newnode
    newnode.next=head
    head=newnode

    return head