#637. Average of Levels in Binary Tree
def averageOfLevels(root):
    
    if not root:
        return []
    
    res = []
    dq = deque([root])

    while dq:
        
        suma = 0
        n = 0
        
        for _ in range(len(dq)):
            curr = dq.popleft()
            suma += curr.val
            n += 1
            if curr.left:
                dq.append(curr.left)
            if curr.right:
                dq.append(curr.right)

        res.append(suma/n)
    
    return res