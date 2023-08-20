def maxAreaOfIsland(grid):

    visit = set()
    max_area = 0
    
    def dfs(i, j):
        if i < 0 or  j < 0 or  i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0 or (i, j) in visit:
            return

        visit.add((i,j))
        
        dfs(i + 1, j)
        dfs(i, j + 1)
        dfs(i - 1, j)
        dfs(i, j - 1)

        return
        
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and (i, j) not in visit:
                area_visited = len(visit)
                dfs(i, j)
                max_area = max(max_area, len(visit) - area_visited)

    return max_area

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
maxAreaOfIsland(grid)