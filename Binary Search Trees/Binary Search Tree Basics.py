class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

def insert(root, val):
    if not root:
        return Node(val)
    
    if root.val == val:
        return root
    elif root.val < val:
        root.right = insert(root.right, val)
    else:
        root.left = insert(root.left, val)

    return root

def search(root, val):
    if not root:
        return None

    def dfs(root):
        if not root:
            return None
         
        if root and root.val == val:
            return root
        
        if val > root.val:
            return dfs(root.right)
        else:
            return dfs(root.left)

    return dfs(root)

def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)
 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)
 
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

 
if __name__ == '__main__':
 
    # Let us create the following BST
    #     50
    #  /     \
    # 30     70
    #  / \ / \
    # 20 40 60 80
 
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)
 
    # Print preorder traversal of the BST
    preorder(r)
    print()
    # Print inorder traversal of the BST : Sorted elements form low to high
    inorder(r)
    print()
    # Print postorder traversal of the BST
    postorder(r)
    print()

    # Search numbres
    print(search(r, 40).val if search(r, 40).val != None else None)
    print(search(r, 0))
    