class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        numIsland=0
        def bfs(r:int,c:int):
            queue=collections.deque([(r,c)])
            grid[r][c]='0'
            while queue:
                row,col=queue.popleft()
                for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nr,nc=row+dr,col+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=='1':
                        grid[nr][nc]='0'
                        queue.append((nr,nc))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    numIsland+=1
                    bfs(i,j)
        return numIsland