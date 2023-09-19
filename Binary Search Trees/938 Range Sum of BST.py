#938. Range Sum of BST

def rangeSumBST(self, root, low, high):
    suma = 0

    def dfs(root):
        nonlocal suma
        if not root:
            return
        
        dfs(root.left)
        if root.val >= low and root.val <= high:
            suma += root.val
        dfs(root.right)

        return

    dfs(root)
    return suma