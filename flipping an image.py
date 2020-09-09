class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        rows=len(A)
        cols=len(A[0])
        
        for i in range(rows):
            A[i]=A[i][::-1]
            for j in range(cols):
                if A[i][j]==0:
                    A[i][j]=1
                else:
                    A[i][j]=0
        
        return A
        
        