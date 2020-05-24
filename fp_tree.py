"""
Implementation of FPTree

https://dzone.com/articles/machinex-understanding-fp-tree-construction
"""

from collections import defaultdict

# TODO: I think this should be part of the FP Tree
def header_dict(filtered_counts):
    """
    Returns a dict to hold
    - frequency across all transactions
    - linked list of the item's occurences when building the fp tree
    - count of co-occurences (along the path) 
    """
    return {k: {'freq': v,
                'node': FPNode(),
                'count': 0
                } for (k, v) in filtered_counts.items()} 

class FPNode:
    def __init__(self, value=None):
        self.value = value 
        self.count = 1
        self.children = {}
    
    def child(self, value):
        return self.children.get(value)

    def add_child(self, value):
        self.children[value] = FPNode(value)

    def increment_count(self):
        self.count += 1


class FPTree:
    def __init__(self):
        self.root = FPNode()

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
            # move prev pointer
            prev = curr