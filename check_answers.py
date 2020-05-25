import ipdb

def valid_solution_line(pattern_size, support, items, min_length, min_support):
    """
    line is an iterable in the format:
    pattern_size, support/count, item1, item2, ... 

    Does the following checks:
    pattern_size == len(items)
    pattern_size >= min_length
    support >= min_support
    """
    assert pattern_size == len(items)
    assert pattern_size >= min_length
    assert support >= min_support
    

def valid_solution(filename, min_length, min_support):
    """
    Reads in a file and checks
    - if each line is a valid solution
    - that there are no duplicate patterns
    """
    unique_items = set()
    for line in open(filename):
        pattern_size, support, *items = line.strip().split(', ')

        pattern_size = int(pattern_size)
        support = int(support)
        items = tuple(items)

        assert items not in unique_items
        unique_items.add(items)

        valid_solution_line(pattern_size, support, items, min_length, min_support)



if __name__ == "__main__":
    valid_solution('slides_solution_1_2.txt', min_length=1, min_support=2)
    valid_solution('slides_solution_2_2.txt', min_length=2, min_support=2)
    valid_solution('slides_solution_3_2.txt', min_length=3, min_support=2)

