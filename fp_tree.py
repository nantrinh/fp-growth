"""
Implementation of FPTree
"""

from collections import defaultdict

class DummyNode:
    """
    Can be used as a head of a linked list
    Keeps track of its tail
    Appends new nodes and updates its tail attribute
    """
    def __init__(self):
        self.tail = self 
        self.next = None
    
    def add(self, node):
        self.tail.next = node
        self.tail = node

class FPNode:
    def __init__(self, value=None, parent=None, root=False):
        self.value = value
        self.count = 1
        self.children = {}
        self.parent = parent
        self.root = root

        # for linked list among nodes with same value
        self.next = None

    def child(self, value):
        return self.children.get(value)

    def add_child(self, value):
        self.children[value] = FPNode(value, self)

    def increment_count(self):
        self.count += 1

    def ancestors(self):
        node = self.parent
        while not node.root:
            yield node
            node = node.parent 

class FPTree:
    def __init__(self):
        self.root = FPNode(root=True)
        # first one is always a dummy
        self.linked_lists = defaultdict(lambda: DummyNode())

    def add(self, transaction):
        """
        Build the FP tree
        """
        prev = self.root

        for item in transaction:
            curr = prev.child(item)
            # if there exists an entry for this item already, increment count
            # else add a new node
            if curr:
                curr.increment_count()
            else:
                prev.add_child(item)
                curr = prev.child(item)
                # keep track of it in linked list
                self.linked_lists[item].add(curr)

            # move prev pointer
            prev = curr
    
    def items(self):
        return self.linked_lists.keys()

    def nodes(self, item):
        # start with the dummy
        curr = self.linked_lists[item]
        # traverse linked list for nodes with the same value
        while curr.next:
            yield curr.next
            curr = curr.next