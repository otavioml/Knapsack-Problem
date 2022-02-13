from read_files import *
from backtracking import *
from branch_and_bound import *
from bnb import *
from dp import *

files = get_test_files()

print("Solucao com backtracking")

for file in files:
    n, w, weights, values = read_files('tests/' + file)
    x = backtracking_knapsack(n, w, weights, values)
    print('Nome do arquivo: ', file, '\t resultado: ', x)

print("Solucao com branch and bound")

for file in files:
    n, w, weights, values = read_files('tests/' + file)
    values, weights = sort_values_and_weights(values, weights, n)
    ppw = []
    for i in range(n):
        ppw.append(values[i]/weights[i])
    x = bnb(w, values, weights, ppw, n)
    print('Nome do arquivo: ', file, '\t resultado: ', x)

# print("Solucao com programacao dinamica")

# for file in files:
#     n, w, weights, values = read_files('tests/' + file)
#     w = int(w)
#     x = dp_knapSack(w, weights, values, n)
#     print('Nome do arquivo: ', file, '\t resultado: ', x)