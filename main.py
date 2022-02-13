from read_files import *
from backtracking import *
from branch_and_bound import *

files = get_test_files()

print("Solucao com backtracking")

for file in files:
    n, w, weights, values = read_files('tests/' + file)
    ans = backtracking_knapsack(n, w, weights, values)
    print('Nome do arquivo: ', file, '\t resultado: ', ans)

print("Solucao com branch and bound")

for file in files:
    n, w, weights, values = read_files('tests/' + file)
    ans = bnb(w, values, weights, n)
    print('Nome do arquivo: ', file, '\t resultado: ', ans)