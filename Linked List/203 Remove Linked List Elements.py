#203. Remove Linked List Elements
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def removeElements(head, val):
    dummy = Node(next=head)
    prev, curr = dummy, head
    
    while curr:
        nxt = curr.next
        
        if curr.val == val:
            prev.next = nxt
        else:
            prev = curr
        
        curr = nxt
    return dummy.next