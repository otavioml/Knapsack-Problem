def backtracking_knapsack(n, w, weights, values):

    if (n == 0 or w == 0):
        return 0

    if (weights[n-1] > w):
        return backtracking_knapsack(n-1, w, weights, values)

    return max(values[n-1] + backtracking_knapsack(n-1, w-weights[n-1], weights, values),
               backtracking_knapsack(n-1, w, weights, values))
