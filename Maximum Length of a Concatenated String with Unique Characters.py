class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxlen = 0
        unique = ['']
        
        
        for word in arr:
            for j in unique:
                tmp = word + j
                if len(tmp)==len(set(tmp)):
                    unique.append(tmp)
                    maxlen = max(maxlen, len(tmp))
                    
        return maxlen

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".