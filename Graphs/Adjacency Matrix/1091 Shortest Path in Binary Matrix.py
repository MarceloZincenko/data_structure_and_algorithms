#1091. Shortest Path in Binary Matrix
def shortestPathBinaryMatrix(grid):
    N = len(grid)
    dq = deque([(0, 0, 1)])
    visit = set((0, 0))
    directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,-1), (-1,1)]

    while dq:
        r, c, length = dq.popleft()

        if r < 0 or c < 0:
            continue
        
        if r >= N or c >= N:
            continue
        
        if grid[r][c]:
            continue
        
        if r == N - 1 and c == N - 1:
            return length
        
        for dr, dc in directions:
            if (r + dr, c + dc) not in visit:
                dq.append((r + dr, c + dc, length + 1))
                visit.add((r + dr, c + dc))
    return -1