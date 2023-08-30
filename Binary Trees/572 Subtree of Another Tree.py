#572. Subtree of Another Tree
def solution(root, subRoot):

    def isSubTree(root, subRoot):    
        if not root:
            return False

        if not subRoot:
            return True
        
        def sameTree(root, subRoot):
            
            if not root and not subRoot:
                return True
            
            if  not root and subRoot:
                return False

            if  root and not subRoot:
                return False
            
            if  root.val != subRoot.val:
                return False
            
            left = sameTree(root.left, subRoot.left)
            right = sameTree(root.right, subRoot.right)
                
            return left and right

        if sameTree(root, subRoot):
            return True
        
        left = isSubTree(root.left, subRoot)
        right = isSubTree(root.right, subRoot)

        return left or right
    
    return isSubTree(root, subRoot)