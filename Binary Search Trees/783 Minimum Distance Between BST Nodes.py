#783. Minimum Distance Between BST Nodes
def solution(root):    
    if not root:
        return 0

    minDiff = float('inf')
    prev = 0
    first_time = True

    def dfs(root):
        nonlocal minDiff, prev, first_time

        if not root:
            return
        
        dfs(root.left)
        if first_time == True:
            first_time= False
            prev = root.val
        else:
            minDiff = min(minDiff, abs(root.val-prev))
            prev = root.val
        dfs(root.right)

        return

    dfs(root)
    return int(minDiff)