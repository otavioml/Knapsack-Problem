from wsgiref import headers
from read_files import *
from backtracking import *
from branch_and_bound import *
import time
import csv

results_file = open('results.csv', 'w')
writer = csv.writer(results_file, delimiter=';')

header = ['Arquivo', 'Tempo de Execucao por Backtracking', 'Tempo de Execucao por Branch and Bound', 'Resultado']

writer.writerow(header)

files = get_test_files()

for file in files:

    results = []

    n, w, weights, values = read_files('tests/' + file)
    results.append(file)

    start_time = time.time()
    ans = backtracking_knapsack(n, w, weights, values)
    end_time = time.time()

    results.append(end_time-start_time)

    start_time = time.time()
    ans = branch_and_bound_knapsack(w, values, weights, n)
    end_time = time.time()
    
    results.append(end_time-start_time)
    results.append(ans)

    writer.writerow(results)


results_file.close()