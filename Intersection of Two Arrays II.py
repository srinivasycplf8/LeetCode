class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = map(collections.Counter, (nums1, nums2))
        return list((a & b).elements())

from collections import Counter
a=[1,1,2,3,33,44,33,2]
b=[3,33,1]
c=Counter(a)
d=Counter(b)
print(c)
print(d)
print(list((c & d).elements()))

# import counter class from collections module 
from collections import Counter 

# Creation of a Counter Class object using 
# string as an iterable data container 
x = Counter("geeksforgeeks") 

# printing the elements of counter object 
for i in x.elements(): 
	print ( i, end = " ") 

g g e e e e k k s s f o r 
