"""
Implementation of FPTree
"""

from collections import defaultdict


class LinkedListNode():
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self, head=None):
        if not head:
            head = LinkedListNode()
        self.head = head
        self.tail = head

    def add(self, value):
        self.tail.next = LinkedListNode(value)
        self.tail = self.tail.next


class FPNode:
    def __init__(self, value=None, parent=None):
        self.value = value
        self.count = 1
        self.children = {}
        self.parent = parent

    def child(self, value):
        return self.children.get(value)

    def add_child(self, value):
        self.children[value] = FPNode(value, self)

    def increment_count(self):
        self.count += 1


class FPTree:
    def __init__(self):
        self.root = FPNode()
        self.linked_lists = defaultdict(lambda: LinkedList())

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

    def all_prefix_paths(self):
        return {k: self.prefix_paths(k) for k in self.linked_lists}

    def prefix_paths(self, item):
        """
        Return prefix paths for this item

        Traverse singly linked list
        For each bottom node for this item, traverse upwards and build path
        """
        paths = []
        curr = self.linked_lists[item].head
        while curr.next:
            # process next bottom node
            tree_curr = curr.next.value
            path_curr = []
            while tree_curr.parent.value:
                # add to path and traverse upwards
                path_curr.append(tree_curr.parent.value)
                tree_curr = tree_curr.parent
            paths.append(path_curr)
            curr = curr.next
        return paths
