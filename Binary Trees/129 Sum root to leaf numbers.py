# 129. sum-root-to-leaf-numbers
def solution(root):
    def dfs(root, suma):
        if not root:
            return 0
        
        suma = suma * 10 + root.val

        if not root.left and not root.right:
            return suma

        left = dfs(root.left, suma)
        right = dfs(root.right, suma)

        return left + right


    return dfs(root, 0)