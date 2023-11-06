# 111. Minimum Depth of Binary Tree
import collections

def minDepth(root):
    if not root:
        return 0
    
    dq = collections.deque([(root, 1)])
    while dq:

        for _ in range(len(dq)):
            curr, depth = dq.popleft()

            if not curr.left and not curr.right:
                return depth
            
            if curr.left:
                dq.append([curr.left, depth + 1])
            if curr.right:
                dq.append([curr.right, depth + 1])