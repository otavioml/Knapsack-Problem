from operator import itemgetter

def sort_values_and_weights(values, weights, n):
    aux = []
    for i in range(n):
        aux.append((values[i], weights[i], values[i]/weights[i]))

    aux = sorted(aux, key=itemgetter(2))
    aux.reverse()
    sorted_values = []
    sorted_weights = []

    for a in aux:
        sorted_values.append(a[0])
        sorted_weights.append(a[1])

    return sorted_values, sorted_weights      

class Node:
    def __init__(self, level, value, weight):
        self.items = []
        self.level = level
        self.value = value
        self.weight = weight
        
            
def bound(node, n, W, values, weights):

    if node.weight >= W:
        return 0
    else:

        bound = node.value
        j = node.level + 1
        total_weight = node.weight

        while j <= n-1 and total_weight + weights[j] <= W:
            total_weight += + weights[j]
            bound += + values[j]
            j+=1

        k = j

        if k <= n-1:
            bound += + (W - total_weight) * (values[k]/weights[k])
        return bound

def branch_and_bound_knapsack(W, values, weights, n):

    values, weights = sort_values_and_weights(values, weights, n)

    pq = []

    v = Node(-1, 0, 0)
    maxProfit = 0
    v.bound = bound(v, n, W, values, weights)

    pq.append(v)

    while pq:

        pq.sort(key=lambda i: i.bound)
        
        v = pq.pop(0)

        if v.bound > maxProfit: 

            node = Node(0, 0, 0)

            node.level = v.level + 1
            node.value = v.value + values[node.level]
            node.weight = v.weight + weights[node.level]

            node.items = v.items.copy()
            node.items.append(node.level)

            if node.weight <= W and node.value > maxProfit: 
                maxProfit = node.value
                
            node.bound = bound(node, n, W, values, weights)

            if node.bound > maxProfit:
                pq.append(node)

            node2 = Node(node.level, v.value, v.weight)
            node2.bound = bound(node2, n, W, values, weights)
            node2.items = v.items.copy()

            if node2.bound > maxProfit:
                pq.append(node2)

    return maxProfit