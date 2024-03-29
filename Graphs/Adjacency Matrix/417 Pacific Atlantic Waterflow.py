def pacificAtlantic(heights):

    rows, cols = len(heights), len(heights[0])
    pac, atl = set(), set()

    def dfs(r, c, visit, prevHeight):
        if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or heights[r][c] < prevHeight:
            return
        
        visit.add((r,c))
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])

    for c in range(cols):
        dfs(0, c, pac, heights[0][c]) #Pacific
        dfs(rows - 1, c, atl, heights[rows - 1][c]) #Atlantic
    
    for r in range(rows):
        dfs(r, 0, pac, heights[r][0]) #Pacific
        dfs(r, cols - 1, atl, heights[r][cols - 1]) #Atlantic
    
    return pac.intersection(atl)

    
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(pacificAtlantic(heights))