# 103. Binary Tree Zigzag Level Order Traversal
def zigzagLevelOrder(self, root):
    
    if not root:
        return []

    res = []
    dq = deque([root])
    
    while dq:
        aux = []
        for _ in range(len(dq)):
            curr = dq.popleft()
            aux.append(curr.val)
            if curr.left:
                dq.append(curr.left)
            if curr.right:
                dq.append(curr.right)
            
        res.append(reversed(aux) if len(res) % 2 else aux)

    return res