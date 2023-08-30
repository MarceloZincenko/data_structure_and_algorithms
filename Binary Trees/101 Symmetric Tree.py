# 101. Symmetric Tree

from collections import deque

def solution(root):

    if not root:
        return True
    
    if not root.left and not root.right:
        return True
    

    dq = deque()
    dq.append(root)
    array = []

    while dq:

        for _ in range(len(dq)):
            curr = dq.popleft()
            
            if curr.left:
                dq.append(curr.left)
                array.append(curr.left.val)
            else:
                array.append('')
            
            if curr.right and curr.right.val != "":
                dq.append(curr.right)
                array.append(curr.right.val)
            else:
                array.append('')

        l = 0
        r = len(array) - 1
        while l < r:
            if array[l] != array[r]:
                return False 
            l += 1
            r -= 1
        
        array = []
            
    return True


