#100 Same Tree

def dfs(p, q):
    if not p and not q:
        return True

    if p and q and p.val == q.val:           
        left = dfs(q.left, p.left)
        right = dfs(q.right, p.right)
        return left and right
    else:
        return False

dfs(p, q)