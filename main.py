from re import X
from read_files import *
from backtracking import *

files = get_test_files()

for file in files:
    n, w, weights, values = read_files('tests/' + file)
    x = backtracking_knapsack(n, w, weights, values)
    print('Nome do arquivo: ', file, '\t resultado: ', x)