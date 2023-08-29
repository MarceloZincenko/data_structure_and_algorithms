# 606. Construct String from Binary Tree

def tree2str(root):
    if not root:
        return ''

    if not root.left and not root.right:
        return str(root.val)

    res = []

    def dfs(t):
        # If the current node is None, do nothing and return
        if t is None:
            return
        res.append(str(t.val))

        # If both left and right children are None, return as there are no more branches to explore
        if t.left is None and t.right is None:
            return
        res.append('(')

        # Recursively call the DFS function for the left child
        dfs(t.left)
        res.append(')')

        # If the right child exists, process it
        if t.right is not None:
            res.append('(')

            # Recursively call the DFS function for the right child
            dfs(t.right)
            res.append(')')

    dfs(root)

    return ''.join(res)