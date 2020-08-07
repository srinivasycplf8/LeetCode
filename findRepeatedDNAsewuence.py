class Solution:
    def findRepeatedDnaSequences(self, s: str) :
        i=0
        counts={}
        newlist=[]



        while i+9<len(s):
            substring=s[i:i+10]
            i=i+1

            if substring in counts:
                counts[substring]+=1
            else:
                counts[substring]=1
            if counts[substring]==2 :
                newlist.append(substring)

        return newlist

            