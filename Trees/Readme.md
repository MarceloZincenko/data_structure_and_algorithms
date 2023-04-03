Resume from different websites

Binary Tree Data Structure Definition:
Binary Tree is defined as a tree data structure where each node has at most 2 children. A tree contains nodes and 2 pointers.Each node of a Binary Tree contains the following parts: Data, Pointer to left child and Pointer to right child.

Other Definitions:
Leaf: A node that has no child is known as the leaf node. It is the last node of the tree. There can be multiple leaf nodes in a tree.
Subtree: The subtree of a node is the tree considering that particular node as the root node.
Depth: The depth of the node is the distance from the root node to that particular node.
Height: The height of the node is the distance from that node to the deepest node of that subtree.
Height of tree: The Height of the tree is the maximum height of any node. This is the same as the height of the root node.
Level: A level is the number of parent nodes corresponding to a given node of the tree.

Why to use Tree Data Structure? 
One reason to use trees might be because you want to store information that naturally forms a hierarchy.
Trees (with some ordering e.g., BST) provide moderate access/search (quicker than Linked List and slower than arrays). 
Trees provide moderate insertion/deletion (quicker than Arrays and slower than Unordered Linked Lists). 
Like Linked Lists and unlike Arrays, Trees don’t have an upper limit on the number of nodes as nodes are linked using pointers.


Important Breath-first traversal: why does not exist a recursive way to do it?
Breadth-first traversal traditionally uses a queue, not a stack. The nature of a queue and a stack are pretty much opposite, so trying to use the call stack (which is a stack, hence the name) as the auxiliary storage (a queue) is pretty much doomed to failure, unless you're doing something stupidly ridiculous with the call stack that you shouldn't be.