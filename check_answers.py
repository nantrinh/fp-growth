import ipdb

def valid_solution_line(line, min_length, min_support):
    """
    line is an iterable in the format:
    pattern_size, support/count, item1, item2, ... 

    Does the following checks:
    pattern_size == len(items)
    pattern_size >= min_length
    support >= min_support
    """
    pattern_size, support, *items = line
    pattern_size = int(pattern_size)
    support = int(support)
    
    assert pattern_size == len(items)
    assert pattern_size >= min_length
    assert support >= min_support

def valid_solution(filename, min_length, min_support):
    """
    Reads in a file and checks if each line is a valid solution
    """
    for line in open(filename):
        valid_solution_line(line.strip().split(', '), min_length, min_support)

if __name__ == "__main__":
    valid_solution('slides_solution_1_2.txt', min_length=1, min_support=2)
    valid_solution('slides_solution_2_2.txt', min_length=2, min_support=2)
    valid_solution('slides_solution_3_2.txt', min_length=3, min_support=2)

