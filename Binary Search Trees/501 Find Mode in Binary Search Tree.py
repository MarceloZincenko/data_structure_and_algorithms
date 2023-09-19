#501. Find Mode in Binary Search Tree

def findMode(root) ->int:

    def get_mode(frec):
        maxi = float(-inf)
        res = []
        for value, count in frec.items():
            if count > maxi:
                    res = []
                    res.append(value)
            elif count == maxi:
                    res.append(value)
            maxi = max(maxi, count)
        return res

    frec = {}

    def dfs(root):
        if not root:
            return
        
        dfs(root.left)
        if root.val in frec:
            frec[root.val] += 1
        else:
            frec[root.val] = 1
        dfs(root.right)

        return
    
    dfs(root)

    return get_mode(frec)