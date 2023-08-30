#226. Invert Binary Tree
from collections import deque

def solution(root):
    if not root:
        return None
    
    dq = deque([root])

    while dq:
        curr = dq.popleft()
        
        temp = curr.left
        curr.left = curr.right
        curr.right = temp

        if curr.left:
            dq.append(curr.left)
        if curr.right:
            dq.append(curr.right)

    return root