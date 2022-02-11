from re import X
from read_files import *
from backtracking import *

n, w, weights, values = read_files('tests/f1_l-d_kp_10_269')

x = backtracking_knapsack(n, w, weights, values)

print(x)