from itertools import combinations

def conditional_fptree_elements(prefix_paths, min_support=1):
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
    sum_counts = sum(counts)
    if sum_counts < min_support:
        return [[], 0]
    else:
        return [longest_common_prefix(paths), sum_counts]

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

def frequent_patterns(item, elements, min_length_of_prefix=1):
    """
    Generates frequent patterns with associated counts.

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
    # print(f'inputs: {item}, {to_combine}, {count}')
    for i in range(min_length_of_prefix, len(to_combine) + 1):
        # print(f'i: {i}')
        C = combinations(to_combine, i) 
        try:
            while True:
                yield [list(next(C)) + [item], count]
        except StopIteration:
            pass 

def write(file_obj, patterns):
    """
    Writes patterns to file in this format:
    pattern_size, support/count, item1, item2, ... 

    Input:
      patterns generator
      yields a list in this format: [['k', 'o'], 3]

    Output: 
      patterns written to file, with their length and support
    """
    try:
        while True:
            p, count = next(patterns)
            # print(p, count)
            if p:
                line = f"{len(p)}, {str(count)}, {', '.join(map(str, p))}\n"
                # print(f"THE LINE IS: {line}")
                file_obj.write(line) 
    except StopIteration:
        pass