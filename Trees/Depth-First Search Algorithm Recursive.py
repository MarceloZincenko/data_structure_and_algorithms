class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

def preorder_dfs_lr_recursive(root):
    """ Traverse the tree in the following order:
    1- Visit Node
    2- Go to left-subtree
    3- Go to right-subtree
    Time complexity: O(n)
    Space complexity: O(n)
    """
    res = []

    if root:
        res.append(root.value)
        res += preorder_dfs_lr_recursive(root.left)
        res += preorder_dfs_lr_recursive(root.right)

    return res

def preorder_dfs_rl_recursive(root):
    """ Traverse the tree in the following order:
    1- Visit Node
    2- Go to right-subtree
    3- Go to left-subtree
    Time complexity: O(n)
    Space complexity: O(n)
    """
    res = []

    if root:
        res.append(root.value)
        res += preorder_dfs_rl_recursive(root.right)
        res += preorder_dfs_rl_recursive(root.left)

    return res

def postorder_dfs_lr_recursive(root):
    """ Traverse the tree in the following order:
    1- Go to left-subtree
    2- Go to right-subtree
    3- Visit Node
    Time complexity: O(n)
    Space complexity: O(n)
    """
    res = []

    if root:
        res = postorder_dfs_lr_recursive(root.left)
        res += postorder_dfs_lr_recursive(root.right)
        res.append(root.value)

    return res

def postorder_dfs_rl_recursive(root):
    """ Traverse the tree in the following order:
    1- Go to right-subtree
    2- Go to left-subtree
    3- Visit Node
    Time complexity: O(n)
    Space complexity: O(n)
    """
    res = []

    if root:
        res = postorder_dfs_rl_recursive(root.right)
        res += postorder_dfs_rl_recursive(root.left)
        res.append(root.value)

    return res

def inorder_dfs_lr_recursive(root):
    """ Traverse the tree in the following order:
    1- Go to left-subtree
    2- Visit Node
    3- Go to right-subtree
    Time complexity: O(n)
    Space complexity: O(n)
    """
    res = []

    if root:
        res = inorder_dfs_lr_recursive(root.left)
        res.append(root.value)
        res += inorder_dfs_lr_recursive(root.right)

    return res

def inorder_dfs_rl_recursive(root):
    """ Traverse the tree in the following order:
    1- Go to right-subtree
    2- Visit Node
    3- Go to left-subtree
    Time complexity: O(n)
    Space complexity: O(n)
    """
    res = []

    if root:
        res = inorder_dfs_rl_recursive(root.right)
        res.append(root.value)
        res += inorder_dfs_rl_recursive(root.left)

    return res

def test_preorder_dfs_lr_recursive() -> None:
    #Define a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node (3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    #Test
    assert preorder_dfs_lr_recursive(root) == [1, 2, 4, 5, 3, 6, 7], "Error"

def test_preorder_dfs_rl_recursive() -> None:
    #Define a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node (3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    #Test
    assert preorder_dfs_rl_recursive(root) == [1, 3, 7, 6, 2, 5, 4], "Error"

def test_postorder_dfs_lr_recursive() -> None:
    #Define a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node (3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    #Test
    assert postorder_dfs_lr_recursive(root) == [4, 5, 2, 6, 7, 3, 1], "Error"

def test_postorder_dfs_rl_recursive() -> None:
    #Define a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node (3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    #Test
    assert postorder_dfs_rl_recursive(root) == [7, 6, 3, 5, 4, 2 ,1], "Error"

def test_inorder_dfs_lr_recursive() -> None:
    #Define a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node (3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    #Test
    assert inorder_dfs_lr_recursive(root) == [4, 2, 5, 1, 6, 3, 7], "Error"

def test_inorder_dfs_rl_recursive() -> None:
    #Define a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node (3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    #Test
    assert inorder_dfs_rl_recursive(root) == [7, 3, 6, 1, 5, 2, 4], "Error"

if __name__ == '__main__':
    test_preorder_dfs_lr_recursive()
    test_preorder_dfs_rl_recursive()
    test_postorder_dfs_lr_recursive()
    test_postorder_dfs_rl_recursive()
    test_inorder_dfs_lr_recursive()
    test_inorder_dfs_rl_recursive()