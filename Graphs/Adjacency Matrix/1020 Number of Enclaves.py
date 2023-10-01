#1020. Number of Enclaves
def numEnclaves(grid):
    M = len(grid)
    N = len(grid[0])

    if M <= 2 or N <= 2:
        return 0 
    
    total = 0
    count = 0
    visited = set()

    def dfs(i, j):
        nonlocal count

        if i < 0 or j < 0 or i == M or  j == N:
            return False
        
        if grid[i][j] == 0 or (i,j) in visited:
            return True
        
        visited.add((i, j))   
        count += 1
        r = dfs(i + 1, j)
        u = dfs(i, j + 1)
        d = dfs(i - 1, j)
        l = dfs(i, j - 1)
        
        return r and u and d and l
    
    for i in range(1, M-1):
        for j in range(1, N-1):
            if grid[i][j] and (i,j) not in visited:
                count = 0
                if dfs(i,j):
                    total += count

    return total