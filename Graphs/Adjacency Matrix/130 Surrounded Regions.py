#130 Surrounded Region
def solve(grid) -> None:

    visit = set()
    
    def dfs(r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 'X' or (r,c) in visit:
            return False
        
        visit.add((r, c))
        island.append((r ,c))
        
        res = False
        if r == 0 or c == 0 or r == len(grid) -1 or c == len(grid[0]) - 1:
            res = True

        res = dfs(r + 1, c) or res
        res = dfs(r, c + 1) or res
        res = dfs(r - 1, c) or res
        res = dfs(r, c - 1) or res

        return res
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "O" and (r, c) not in visit:
                island = list()
                res =  dfs(r, c)
                if res == False:
                    for e in island:
                        grid[e[0]][e[1]] = 'X'
    
    return

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solve(board)