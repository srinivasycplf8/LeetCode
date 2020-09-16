class Solution:
    def mark(self,grid,i,j,rows,cols):
        if i<0 or j<0 or i>=rows or j>=cols or grid[i][j]!="1":
            return
        grid[i][j]="2"
        self.mark(grid,i-1,j,rows,cols)
        self.mark(grid,i+1,j,rows,cols)
        self.mark(grid,i,j-1,rows,cols)
        self.mark(grid,i,j+1,rows,cols)


    def numIslands(self, grid: List[List[str]]) -> int:
        if grid==[]:
            return 0
        rows=len(grid)
        cols=len(grid[0])
        islands=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    self.mark(grid,i,j,rows,cols)
                    islands+=1
        
        return islands

       