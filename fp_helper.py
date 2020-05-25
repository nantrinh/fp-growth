from itertools import combinations

def conditional_fptree_elements(prefix_paths):
    """
    Input:
    [[iterable path, count]]
    For example: [['kemo', 1], ['keo', 1], ['km', 1]],

    Output:
    [longest common prefix among inputs, sum of all counts in input] 
    For example: [['k', 3]]
    """
#    print(f'prefix_paths: {prefix_paths}')

    paths, counts = zip(*prefix_paths)
    return [longest_common_prefix(paths), sum(counts)]

def longest_common_prefix(sorted_iterable):
    """
    Input is an iterable of SORTED iterables
    Output is a list of the longest common prefix

    Since the input is sorted, the lcp between the first and last element
    is also the lcp for all elements. 
    """
    if len(sorted_iterable) == 1:
        return list(sorted_iterable[0]) if sorted_iterable[0] else [] 
    else:
        i1 = sorted_iterable[0]
        i2 = sorted_iterable[-1]
    
        # using zip automatically means you only iterate as much as the
        # min length of i1 and i2
        return [x for (x, y) in zip(i1, i2) if x == y] 

def frequent_patterns(item, elements):
    """
    This is a generator function.

    Input:
      item: usually a char or int  
      Example: 'o'
      
      elements: [[conditional frequent patterns], count]
      Example: [['k', 'e'], 3]

    Output:
      yields all possible subsets of elements and item
      Example: 
      [[['k', 'o'], 3], [['e', 'o'], 3], [['e', 'k', 'o'], 3]],
    """
    to_combine, count = elements
    print(f'inputs: {item}, {to_combine}, {count}')
    for i in range(1, len(to_combine) + 1):
        print(f'i: {i}')
        C = combinations(to_combine, i) 
        try:
            while True:
                yield [list(next(C)) + [item], count]
        except StopIteration:
            pass