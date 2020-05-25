import fp_tree as fpt

def examples():
    return [_gfg_example()]

def _gfg_example():
    example = {
        'filtered_transactions': ['kemoy', 'keoy', 'kem', 'kmy', 'keo'],
        'counts': {'k': 5, 'e': 4, 'm': 3, 'o': 3, 'y': 3},
        'traversal_order': 'yomek',
        'count_order': [[5, 4, 2, 1, 1], [5, 4, 2, 1], [5, 4, 2], [5, 1, 1], [5, 4, 2]],
        'll_order': [[1, 1, 1], [1, 2], [2, 1], [4], [5]],
        'prefix_paths': {
            'y': [[['k', 'e', 'm', 'o'], 1], [['k', 'e', 'o'], 1], [['k', 'm'], 1]],
            'o': [[['k', 'e', 'm'], 1], [['k', 'e'], 2]],
            'm': [[['k', 'e'], 2], [['k'], 1]],
            'e': [[['k'], 4]],
            'k': [[None, 0]]
        },
        'lcp': {
            'y': [['k'], 3],
            'o': [['k', 'e'], 3],
            'm': [['k'], 3],
            'e': [['k'], 4],
            'k': [[], 0],
        },
        'frequent_patterns': {
            'y': [[set(['k', 'y']), 3]],
            'o': [[set(['k', 'o']), 3], [set(['e', 'o']), 3], [set(['e', 'k', 'o']), 3]],
            'm': [[set(['k', 'm']), 3]],
            'e': [[set(['e', 'k']), 4]],
            'k': []
        },
        'tree': None,
    }
    tree = fpt.FPTree()
    for t in example['filtered_transactions']:
        tree.add(t)
    example['tree'] = tree
    return example
