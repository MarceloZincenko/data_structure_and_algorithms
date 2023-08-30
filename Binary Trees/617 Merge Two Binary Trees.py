# 617. Merge Two Binary Trees
from collections import deque

class TreeNode():
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right
        
def solution(root1, root2):
    if not root1 and not root2:
        return None
    
    if root1 and not root2:
        return root1

    if not root1 and root2:
        return root2

    dq1 = deque([root1])
    dq2 = deque([root2])

    while dq1 and dq2:
        for _ in range(len(dq1)):
            curr1 = dq1.popleft()
            curr2 = dq2.popleft()

            curr1.val += curr2.val

            if curr1.left and curr2.left:
                dq1.append(curr1.left)
                dq2.append(curr2.left)
            elif curr1.left and not curr2.left:
                dq1.append(curr1.left)
                dq2.append(TreeNode())
            elif curr2.left and not curr1.left:
                curr1.left = TreeNode()
                dq1.append(curr1.left)
                dq2.append(curr2.left)

            if curr1.right and curr2.right:
                dq1.append(curr1.right)
                dq2.append(curr2.right)
            elif curr1.right and not curr2.right:
                dq1.append(curr1.right)
                dq2.append(TreeNode())
            elif curr2.right and not curr1.right:
                curr1.right = TreeNode()
                dq1.append(curr1.right)
                dq2.append(curr2.right)

    return root1