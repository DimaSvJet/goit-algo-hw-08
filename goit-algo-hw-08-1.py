import heapq

nums = [4, 10, 3, 5, 1]
heapq.heapify(nums)
print(nums)  # Output: [1, 4, 3, 5, 10]

heapq.heappush(nums, 0)
print(nums)  # Output: [0, 4, 1, 5, 10, 3]
print(len(nums))

def optimiz_cost(pile):
    summ_nodes_of_pile = 0
    if not pile:
        return -1
    while len(pile) >1:
        min1 = heapq.heappop(nums)
        min2 = heapq.heappop(nums)
        new_nobe = min1 + min2
        summ_nodes_of_pile += new_nobe
        heapq.heappush(pile,  new_nobe)
    return summ_nodes_of_pile
print(optimiz_cost(nums))