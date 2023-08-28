#145. Binary Tree Postorder Traversal

def solution(root):
    res = []

    def dfs(root):
        if root:
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        return
    
    dfs(root)

    return res