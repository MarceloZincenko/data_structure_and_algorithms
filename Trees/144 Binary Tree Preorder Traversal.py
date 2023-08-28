#144. Binary Tree Preorder Traversal

def solution(root):
    res = []

    def dfs(root):
        if root:
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        return
    
    dfs(root)

    return res