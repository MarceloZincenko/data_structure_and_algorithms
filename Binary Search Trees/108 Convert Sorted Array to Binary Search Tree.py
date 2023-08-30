
# 108. Convert Sorted Array to Binary Search Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if len(nums) == 1:
        return TreeNode(nums[0])
    
    def insert(arr):
        if not arr:
            return None
        # find middle index
        mid = (len(arr)) // 2
    
        # make the middle element the root
        root = TreeNode(arr[mid])
    
        # left subtree of root has all
        # values <arr[mid]
        root.left = insert(arr[:mid])
    
        # right subtree of root has all
        # values >arr[mid]
        root.right = insert(arr[mid+1:])
        
        return root

    return insert(nums)

sortedArrayToBST([-10,-3,0,5,9])