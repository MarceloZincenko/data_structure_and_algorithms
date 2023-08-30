class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

def preorder_dfs_lr(root):
    """ Traverse the tree in the following order:
    1- Visit Node
    2- Go to left-subtree
    3- Go to right-subtree
    Time complexity: O(n)
    Space complexity: O(n)
    """
    res = []
    
    if root:
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.value)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
    
    return res

def preorder_dfs_rl(root):
    """ Traverse the tree in the following order:
    1- Visit Node
    2- Go to right-subtree
    3- Go to left-subtree
    Time complexity: O(n)
    Space complexity: O(n)
    """
    res = []
    
    if root:
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.value)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

    
    return res

def test_preorder_dfs_lr() -> None:
    #Define a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node (3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    #Test
    assert preorder_dfs_lr(root) == [1, 2, 4, 5, 3, 6, 7], "Error"

def test_preorder_dfs_rl() -> None:
    #Define a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node (3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    #Test
    assert preorder_dfs_rl(root) == [1, 3, 7, 6, 2, 5, 4], "Error"

if __name__ == '__main__':
    test_preorder_dfs_lr()
    test_preorder_dfs_rl()
