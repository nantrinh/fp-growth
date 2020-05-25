def valid_solution_line(pattern_size, support, items, min_length, min_support):
    """
    line is an iterable in the format:
    pattern_size, support/count, item1, item2, ... 

    Does the following checks:
    pattern_size == len(items)
    pattern_size >= min_length
    support >= min_support
    """
    try:
        assert pattern_size == len(items)
        assert pattern_size >= min_length
        assert support >= min_support
    except AssertionError as err:
        print(err)
        print(f'{pattern_size}, {support}, {items}. expected min_length: {min_length} min_support: {min_support}')

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

def check_slides_solutions():
    valid_solution('slides_solution_1_2.txt', min_length=1, min_support=2)
    valid_solution('slides_solution_2_2.txt', min_length=2, min_support=2)
    valid_solution('slides_solution_3_2.txt', min_length=3, min_support=2)

def same_solution(solution, my_answer):
    s_list = [] 
    my_list = [] 

    for line in open(solution):
        pattern_size, support, *items = line.strip().split(', ')
        s_list.append((pattern_size, support, set(items)))

    for line in open(my_answer):
        pattern_size, support, *items = line.strip().split(', ')
        my_list.append((pattern_size, support, set(items)))

    if len(my_list) != len(s_list):
        print(f'my len: {len(my_list)}, expected len: {len(s_list)}')
    for a in my_list:
        if a not in s_list:
            print('===')
            print(a in s_list)
            print(a)

if __name__ == "__main__":
    # check_slides_solutions()
 #   import sys

    # python check_answers.py output.txt 3 2
#     filename, min_length, min_support = sys.argv[1:]
#     min_length, min_support = int(min_length), int(min_support)
#     valid_solution(filename, min_length, min_support)
    same_solution('slides_solution_1_2.txt', 'output.txt')
