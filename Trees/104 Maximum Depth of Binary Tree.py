#104. Maximum Depth of Binary Tree

#BFS
from collections import deque

def solution(root):
    q = deque()

    if root:
        q.append(root)
    
    level = 0

    while q:

        for i in range(len(q)):
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        
        level += 1

    return level

#DFS Iterative
def solution(root):
    if not root:
        return 0
    
    stack = [[root, 1]]
    res = 0

    while stack:
        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
            
    return res

#DFS induction
def solution(root):
    def dfs(root):
        if not root:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)
                    
        return 1 + max(left, right)

    return dfs(root)
