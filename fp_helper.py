from itertools import combinations
from collections import defaultdict
import ipdb

def frequent_patterns(tree, min_length, min_support):
    """
    Generates frequent patterns with associated counts.
    """

    for item in tree.items():
        print(f'PROCESSING ITEM {item}')
        # this result dictionary has the format
        # {tuple of pattern: support}
        # for example: {('d', 'c', 'a'): 3}
        # its entries and counts will be modified by the code below it
        results = defaultdict(lambda: 0) 
        # traverse the linked list for the item
        for node in tree.nodes(item):
            leaf_count = node.count
            # they're all going to start with the same value
            temp_paths = [[item]]
            for ancestor in node.ancestors():
                if not temp_paths:
                    temp_paths.append(ancestor.value)
                else:
                    temp_paths.extend([p + [ancestor.value] for p in temp_paths])
            update_counts(results, temp_paths, leaf_count)
        for (k, v) in results.items():
            if len(k) >= min_length and v >= min_support:
                yield (k, v) 

def update_counts(results, paths, leaf_count):
    for p in paths:
        results[tuple(p)] += leaf_count

def yield_results(results, min_length, min_support):
    for (k, v) in results:
        if len(k) >= min_length and v >= min_support:
            yield (k, v) 

def write(file_obj, pattern, support):
    """
    Writes patterns to file in this format:
    pattern_size, support/count, item1, item2, ... 

    Input:
      pattern iterable, support
      e.g., ('e', 'd', 'a'), 2
    """

    line = f"{len(pattern)}, {support}, {', '.join(map(str, pattern))}\n"
    print(f"THE LINE IS: {line}")
    file_obj.write(line) 