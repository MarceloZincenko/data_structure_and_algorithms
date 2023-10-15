#206. Reverse Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverseList(head):
    
    curr = head
    prev = None
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev
        