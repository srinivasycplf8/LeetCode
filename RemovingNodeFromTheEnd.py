 #Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) :
        current=self.head
        count=0
        while current:
            count+=1
        index=count-n
        initial=0
        while current and initial!=index+1:
            current=current.next
            initial+=1
        
        current.next=current.next.next
        
        



