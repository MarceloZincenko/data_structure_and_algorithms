#112. Path sum (root to leaf)
from collections import deque

def solution(root, targetSum):
    if not root:
        return False

    deque = deque()
    deque.append((root, root.val))

    while deque:

        curr, suma = deque.popleft()

        if not curr.left and not curr.right and suma == targetSum:
            return True
        
        if curr.left:
            deque.append((curr.left, suma + curr.left.val))

        if curr.right:
            deque.append((curr.right, suma + curr.right.val))
    
    return False