from hashlib import new
from operator import itemgetter

class Item():
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def sort_values_and_weights(values, weights, n):
    aux = []
    for i in range(n):
        aux.append((values[i], weights[i], values[i]/weights[i]))

    aux = sorted(aux, key=itemgetter(2))
    aux.reverse()
    # sorted_values = []
    # sorted_weights = []
    ans = []

    for a in aux:
        # sorted_values.append(a[0])
        # sorted_weights.append(a[1])
        ans.append(Item(a[1], a[0]))

    return ans



class Node():
    def __init__(self, level, profit, bound, weight):
        self.level = level
        self.profit = profit
        self.bound = bound
        self.weight = weight

def cmp(a, b):
    r1 = (a.value/a.weight)
    r2 = (b.value/b.weight)
    return r1 > r2


def bound(u, n, W, arr):
    if (u.weight >= W):
        return 0

    profit_bound = u.profit
    j = u.level + 1
    totweight = u.weight

    while((j < n) and (totweight + arr[j].weight <= W)):
        totweight += arr[j].weight
        profit_bound += arr[j].value
        j += 1

    if (j < n):
        profit_bound += (W - totweight) * arr[j].value/arr[j].weight

    return profit_bound


def branch_and_bound_knapsack(W, values, weights, n):

    arr = sort_values_and_weights(values, weights, n)

    Q = []
    u = Node(None, None, None, None)
    v = Node(None, None, None, None)

    u.level = -1
    u.profit = 0
    u.weight = 0
    Q.append(u)