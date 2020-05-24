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