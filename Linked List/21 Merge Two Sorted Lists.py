#21. Merge Two Sorted Lists
def mergeTwoLists(list1, list2):
    
    curr1 = list1
    curr2 = list2
    
    if curr1 == None and curr2 == None:
        return None
    
    if curr1 == None:
        return curr2
    
    if curr2 == None:
        return curr1

    # set the head
    if curr1.val <= curr2.val:
        head = curr1
        curr1 = curr1.next
    else:
        head = curr2
        curr2 = curr2.next
    
    curr = head
    while curr1 and curr2:
        if curr1.val <= curr2.val:
            curr.next = curr1
            curr1 = curr1.next
        else:
            curr.next = curr2
            curr2 = curr2.next
        curr = curr.next
        
    if curr1:
        curr.next = curr1
    if curr2:
        curr.next = curr2
    
    return head