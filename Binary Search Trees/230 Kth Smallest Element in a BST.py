# 230. Kth Smallest Element in a BST
def solution(root,k):
    count = 0
    value = 0
    def dfs(root):
        nonlocal count, value

        if root:
            dfs(root.left)
            if count == k-1:
                value = root.val
            count += 1
            dfs(root.right)

    dfs(root)
    return value

