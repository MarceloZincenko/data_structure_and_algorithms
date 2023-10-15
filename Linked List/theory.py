# Definition
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

# Create a Linked List with string values
String = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
String.next = B
B.next = C
C.next = D
D.next = E
E.next = F
F.next = G

# Create a Linked List with numeric values
Numeric = Node(1)
N2 = Node(2)
N3 = Node(3)
N4 = Node(4)
N5 = Node(5)
N6 = Node(6)
N7 = Node(7)
Numeric.next = N2
N2.next = N3
N3.next = N4
N4.next = N5
N5.next = N6
N6.next = N7

#Move on the list
def print_linked_list(head):
    curr = head
    while curr:
        print(curr.value)
        curr = curr.next

print('print_linked_list')
print_linked_list(String)

def print_linked_list_recursive(head):
    if head == None:
        return
    print(head.value)
    print_linked_list_recursive(head.next)

print('print_linked_list_recursive')
print_linked_list_recursive(String)

#collect elements of a linked list
def collect_elements(head):
    res = []
    curr = head
    while curr:
        res.append(curr.value)
        curr = curr.next

    return res

print('collect_elements')
print(collect_elements(String))

def collect_elements_recursive(head):
    res = []
    def get_elements(head):
        if head == None:
            return
        res.append(head.value)
        get_elements(head.next)

    get_elements(head)
    return res

print('collect_elements_recursive')
print(collect_elements_recursive(String))

def collect_elements_recursive2(head, res):
    if head == None:
        return
    res.append(head.value)
    collect_elements_recursive2(head.next, res)
    return res

print('collect_elements_recursive2')
print(collect_elements_recursive2(String, []))

def insert_node_begining(head, value):
    if head == None:
        return Node(value)
    else:
        temp = Node(value)
        temp.next = head
        return temp

print('insert_node_begining')
print(collect_elements_recursive(insert_node_begining(String, 'Z')))

def insert_node_end(head, value):
    if head == None:
        return Node(value)
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.nextf = Node(value)

    return head

print('insert_node_end')
print(collect_elements_recursive(insert_node_end(String, 'H')))

def insert_node_position(head, value, pos):

    if pos == 0:
        tmp = Node(value)
        tmp.next = head
        head = tmp
        return head
    
    if head == None and pos > 0:
        return None

    curr = head
    i = 0

    while i<pos and curr.next != None:
        curr = curr.next
        i += 1
    
    tmp = Node(value)
    tmp.next = curr.next
    curr.next = tmp

    return head

print('insert_node_position')
print(collect_elements_recursive(insert_node_position(String, 'Z',0)))

#sum values
def sum_values(head):
    curr = head
    suma = 0
    while curr:
        suma += curr.value
        curr = curr.next
    return suma

def sum_values_recursive(head):
    
    if head == None:
        return 0
    
    return head.value + sum_values_recursive(head.next)

def find_value(head, target):

    curr = head
    while curr:
        if curr.value == target:
            return True
        curr = curr.next
    
    return False
    
def find_value_recursive(head, target):

    if head == None:
        return False
    if head.value == target:
        return True
    
    return find_value_recursive(head.next, target)

