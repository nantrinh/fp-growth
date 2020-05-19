# assuming data can fit in memory

# the result is a list of sets
# each set corresponds to a transaction
#
# Example:
# [
#   {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29},
#   {32, 30, 31},
#   {33, 34, 35},
#   {36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46},
#   {48, 47, 38, 39}
# ]
datalist = [set([int(x) for x in line.split()]) for line in open('retail_25k.dat')] 

# Try FP trees
# https://docs.rapidminer.com/latest/studio/operators/modeling/associations/fp_growth.html