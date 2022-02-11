#




def backtracking_knapsack (n, w, weights, values):

    if (n == 0 or w == 0):
        return 0


    return max(values[n-1] + backtracking_knapsack(n-1, w-weights[n-1], weights, values),
               backtracking_knapsack(n-1, w, weights, values))

# val = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50
# n = len(val)
# print (backtracking_knapsack(n, W, wt, val))