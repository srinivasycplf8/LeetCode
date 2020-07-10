class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #every time you need to track two pointers one is 
        #startign point and ending pointer
        #starting pointer and ending pointer starts from 0 index
        #startign poitner remains at zero till it won't see repeated characthers"dvdf"
        counts={}
        start_tracker=0
        max_length=0
        for end_tracker in range(len(s)):
            if s[end_tracker] in counts:
                #till now our starting pointer is at zero 
                #now the d is initially at 0 so 0+1 =1
                #so the tracker moves from to 1st position
                #so that it will get rid of the repeating character 
                #of initial "d"
                start_tracker=max(start_tracker,counts[s[end_tracker]]+1)
             #if there's no repating character it goes on
            counts[s[end_tracker]]=end_tracker
            max_length=max(max_length,end_tracker-start_tracker+1)
        return max_length
        