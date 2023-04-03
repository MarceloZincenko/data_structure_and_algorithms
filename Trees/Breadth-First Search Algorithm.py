import collections
import pytest


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


def lr_bfs(root: Node) -> None:
    """ 
    Traverse the tree by level from left to right
    n: number of nodes
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    res = []

    if root:
        deque = collections.deque([root])

        while deque:
            tmp = []
            for _ in range(len(deque)):
                curr = deque.pop()
                tmp.append(curr.value)
                if curr.left:
                    deque.appendleft(curr.left)
                if curr.right:
                    deque.appendleft(curr.right)
            res.append(tmp)

    return res


def rl_bfs(root: Node) -> None:
    """ 
    Traverse the tree by level from right to left 
    n: number of nodes
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    res = []

    if root:
        deque = collections.deque([root])

        while deque:
            tmp = []
            for _ in range(len(deque)):
                curr = deque.pop()
                tmp.append(curr.value)
                if curr.right:
                    deque.appendleft(curr.right)
                if curr.left:
                    deque.appendleft(curr.left)
            res.append(tmp)

    return res

def test_lr_bfs() -> None:
    #Define a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node (3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    #Test
    assert lr_bfs(root) == [[1], [2, 3], [4, 5, 6, 7]], "Error"

def test_rl_bfs() -> None:
    #Define a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node (3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    #Test
    assert rl_bfs(root) == [[1], [3, 2], [7, 6, 5, 4]], "Error"

if __name__ == '__main__':
    test_lr_bfs()
    test_rl_bfs()

