# 543. Diameter of Binary Tree
def solution(root):
    res = 0

    def dfs(root):
        nonlocal res

        if not root:
            return 0
        
        left = dfs(root.left)
        right = dfs(root.right)
        res = max(res, left + right)

        return 1 + max(left, right)

    dfs(root)
    return res