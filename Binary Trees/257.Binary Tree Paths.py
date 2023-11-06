#257. Binary Tree Paths
def binaryTreePaths(root):

    res = []        
    
    def dfs(root, path):
        if not root:
            return
        
        path.append(str(root.val))

        if not root.left and not root.right:
            res.append(path.copy())

        dfs(root.left, path.copy())
        dfs(root.right, path.copy())

    dfs(root, [])

    str_res = []
    for e in res:
        str_res.append('->'.join(e))

    return str_res