#102. Binary Tree Level Order Traversal

def solution(root):
    if not root:
        return []

    res = []

    dq = deque()
    dq.append(root)

    while dq:
        aux = []
        for _ in range(len(dq)):
            curr = dq.popleft()

            aux.append(curr.val)

            if curr.left:
                dq.append(curr.left)
            if curr.right:
                dq.append(curr.right)
            
        res.append(aux)
    
    return res

