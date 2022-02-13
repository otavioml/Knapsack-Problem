from operator import itemgetter

def sort_values_and_weights(values, weights, n):
    aux = []
    for i in range(n):
        aux.append((values[i], weights[i], values[i]/weights[i]))

    aux = sorted(aux, key=itemgetter(2))
    aux.reverse()
    sorted_values = []
    sorted_weights = []
    # ans = []

    for a in aux:
        sorted_values.append(a[0])
        sorted_weights.append(a[1])
        # ans.append(Item(a[1], a[0]))

    return sorted_values, sorted_weights

# class Item():
#     def __init__(self, weight, value):
#         self.weight = weight
#         self.value = value


# class Node():
#     def __init__(self, level, profit, bound, weight):
#         self.level = level
#         self.profit = profit
#         self.bound = bound
#         self.weight = weight

# def cmp(a, b):
#     r1 = (a.value/a.weight)
#     r2 = (b.value/b.weight)
#     return r1 > r2


# def bound(u, n, W, arr):

#     if (u.weight > W):
#         return 0

#     profit_bound = u.profit

#     j = u.level + 1
#     totweight = u.weight

#     while((j < n) and (totweight + arr[j].weight <= W)):

#         totweight += arr[j].weight
#         profit_bound += arr[j].value
#         j += 1

#     if (j < n):
#         profit_bound += (W - totweight) * arr[j].value/arr[j].weight

#     return profit_bound


# def branch_and_bound_knapsack(W, values, weights, n):

#     arr = sort_values_and_weights(values, weights, n)

#     Q = []
#     u = Node(None, None, None, None)
#     v = Node(None, None, None, None)

#     u.level = -1
#     u.profit = 0
#     u.weight = 0
#     Q.append(u)

#     maxProfit = 0
#     while(len(Q)):

#         Q.sort(key=lambda a: a.bound)
#         Q.reverse()

#         u = Q[0]
#         Q.pop(0)

#         if (u.level == -1):
#             v.level = 0

#         if (u.level == n-1):
#             continue

#         v.level = u.level + 1

#         v.weight = u.weight + arr[v.level].weight
#         v.profit = u.profit + arr[v.level].value

#         if (v.weight <= W and v.profit > maxProfit):
#             maxProfit = v.profit

#         v.bound = bound(v, n, W, arr)

#         if (v.bound >= maxProfit):
#             Q.append(v)

#         v.weight = u.weight
#         v.profit = u.profit
#         v.bound = bound(v, n, W, arr)

#         if (v.bound >= maxProfit):
#             Q.append(v)

#     return maxProfit


# W = 10
# n = 4
# v = [12, 42, 25, 40]
# w = [3, 7, 5, 4]

# x = branch_and_bound_knapsack(W, v, w, n)
# print(x)


# # item1 = Item(4, 40)
# # item2 = Item(7, 42)
# # item3 = Item(5, 25)
# # item4 = Item(3, 12)

# # l = []
# # l.append(item1)
# # l.append(item4)
# # l.append(item3)
# # l.append(item2)

# # for l1 in l:
# #     print(l1.weight, l1.value)

# # l.sort(key=lambda a: a.value/a.weight)
# # l.reverse()

# # print("*****")

# # for l1 in l:
# #     print(l1.weight, l1.value)

# # l.pop(0)

# # print("*****")

# # for l1 in l:
# #     print(l1.weight, l1.value)