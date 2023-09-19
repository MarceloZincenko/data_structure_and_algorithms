# 897. Increasing Order Search Tree

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def increasingBST(root):
    res = []
    def inOrder(root):
        if not root:
            return
        inOrder(root.left)
        res.append(root.val)
        inOrder(root.right)
        return res
    array = inOrder(root)

    root = cur = Node(array[0])
    for i in range(1, len(array)):
        cur.right = Node(array[i])
        cur = cur.right
    return root