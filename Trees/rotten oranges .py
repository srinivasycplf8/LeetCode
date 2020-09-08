
class Solution(object):
    def orangesRotting(self, grid):
        queue = []
        ## add initial rotten oranges
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i,j])
                            
        ans = 0
        while queue:
            c = len(queue)
            for i in range(c):
                i,j = queue.pop(0)
                if j < len(grid[0])-1:
                    if grid[i][j+1] == 1:
                        grid[i][j+1] = 2
                        queue.append([i, j+1])
                if j - 1 >= 0:
                    if grid[i][j-1] == 1:
                        grid[i][j-1] = 2
                        queue.append([i, j-1])
                if i - 1 >= 0:
                    if grid[i - 1][j] == 1:
                        grid[i-1][j] = 2
                        queue.append([i-1, j])
                if i < len(grid)-1:
                    if grid[i + 1][j] == 1:
                        grid[i+1][j] = 2
                        queue.append([i+1, j])

            if queue:
                ans += 1
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return ans