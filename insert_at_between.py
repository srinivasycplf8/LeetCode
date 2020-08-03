class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None


def insertNodeAtPosition(head, data, position):
    newnode=Node(data)
    if head is  None:
        return newnode
    current=head
    pos=0
    while pos<position:
        previous=current
        current=current.next
        pos+=1
    newnode.next=current
    previous.next=newnode

    return head