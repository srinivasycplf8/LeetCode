# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head=None
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current=l1
        new=[]
        while current!=None:
            new.append(current.val)
            current=current.next
        current2=l2
        new2=[]
        while current2!=None:
            new2.append(current2.val)
            current2=current2.next

        res1 = ("".join(map(str, new[::-1]))) 
        res2 = ("".join(map(str, new2[::-1]))) 
        result=str(int(res1)+int(res2))
        final=result[::-1]
        final=(list(map(int, final))) 
        i=0
        result=ListNode(0)
        resulttail=result
        while i<len(final):
            resulttail.next=ListNode(final[i])
            i+=1
            resulttail=resulttail.next
        
        return result.next
            