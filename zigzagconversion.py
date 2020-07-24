class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        step=1
        pos = 1
        new = {}
        for c in s:
            if pos not in new:
                new[pos] = c
            else:
                new[pos]+=c
            pos+=step
            if pos==1 or pos==numRows:
                step*=-1
        result = ""
        for i in range(1, numRows+1):
            try:
                result+=new[i]
            except:
                return result

        return result
   

        