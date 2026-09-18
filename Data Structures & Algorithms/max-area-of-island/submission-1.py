class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        rows,cols=len(grid),len(grid[0])
        def bfs(r:int,c:int)->int:
            curr_area=1
            queue=collections.deque([(r,c)])
            grid[r][c]=0
            while queue:
                row,col=queue.pop()
                for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nr=row+dr
                    nc=col+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        queue.append((nr,nc))
                        grid[nr][nc]=0
                        curr_area+=1
            return curr_area
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    max_area=max(bfs(i,j),max_area)
        return max_area
                        
            