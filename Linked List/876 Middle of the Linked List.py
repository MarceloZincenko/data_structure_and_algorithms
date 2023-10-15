#876. Middle of the Linked List
def middleNode(head):
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    if not fast.next:
        return slow
    else:
        return slow.next