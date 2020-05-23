from collections import defaultdict

class Node:
    def __init__(self, value=None):
        self.value = value 
        self.count = 0

def header_dict(filtered_counts):
    """
    Returns a dict to hold
    - frequency across all transactions
    - linked list of the item's occurences when building the fp tree
    - count of co-occurences (along the path) 
    """
    return {k: {'freq': v,
                'node': Node(),
                'count': 0
                } for (k, v) in filtered_counts.items()} 
