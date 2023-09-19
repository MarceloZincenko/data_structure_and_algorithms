# 530. Minimum Absolute Difference in BST

def getMinimumDifference(root) -> int:
    
    min_abs_dif = float(inf)
    prev_val = None
    def dfs(root):
        nonlocal min_abs_dif, prev_val

        if not root:
            return 

        dfs(root.left)
        if prev_val != None:
            min_abs_dif = min(min_abs_dif, abs(prev_val-root.val))
        prev_val = root.val
        dfs(root.right)
        
        return
    
    dfs(root)
    return min_abs_dif