class Solution:
    def compress(self, chars: List[str]) -> int:
        index=0
        i=0
        if len(chars)==1:
            return 1
        while i < len(chars):
            j=i
            while j<len(chars) and chars[j]==chars[i]:
                j+=1
            
            if j-i>1:
                chars[index]=chars[i]
                index+=1
                count=str(j-i)
                for k in count:
                    chars[index]=k
                    index+=1
            
            else:
                chars[index]=chars[i]
                index+=1
                    
            
            i=j
                
        return index
            