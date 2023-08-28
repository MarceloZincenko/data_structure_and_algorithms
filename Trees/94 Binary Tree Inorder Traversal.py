#94. Binary Tree Inorder Traversal

def solution(root):
    res = []

    def dfs(root):
        if root:
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        return
    
    dfs(root)

    return res