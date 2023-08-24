
def solution(n , edges):
    # Create adjacency list
    graph = {i:set() for i in range(n)}
    for start, end in edges:
        graph[start].add(end)
        graph[end].add(start)

    visit = set()

    def dfs(i):
        if i in visit:
            return
        
        visit.add(i)

        for j in graph[i]:
            dfs(j)

    count = 0
    for i in range(n):
        if i not in visit:
            count += 1
            dfs(i) 

    return count


n = 7
edges = [[0, 1], [1, 2],[6, 5] ,[3, 4]]
print(solution(n, edges))