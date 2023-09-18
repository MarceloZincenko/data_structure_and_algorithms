#98. Validate Binary Search Tree
def isValidBST(root) -> bool:
    
    first = False
    validate = True
    prev = 0

    def dfs(root):
        nonlocal first, validate, prev

        if not root:
            return

        dfs(root.left)
        if first == False:
            first = True
        else:
            if prev >= root.val:
                validate = False
        prev = root.val

        dfs(root.right) 
        
        return 

    dfs(root)
    return validate