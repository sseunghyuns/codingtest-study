'''
https://leetcode.com/problems/number-of-islands/submissions/
'''

class Solution:
    def dfs(self, grid, v):
        x, y = v
        
        if x <0 or x>=len(grid) or y<0 or y>=len(grid[0]):
            return False
            
        if grid[x][y] == '1':
            grid[x][y] = '0'
            
            self.dfs(grid, (x+1, y))
            self.dfs(grid, (x-1, y))
            self.dfs(grid, (x, y+1))
            self.dfs(grid, (x, y-1))  
            return True
        
        return False
    
    def numIslands(self, grid: List[List[str]]) -> int:
        answer=0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.dfs(grid, (i, j))==True:
                    answer+=1

        return answer        

