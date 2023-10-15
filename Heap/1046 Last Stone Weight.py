import heapq
def lastStoneWeight(stones):
    
    # Initialize a list with some values
    values = [-x for x in stones]

    # Convert the list into a heap
    heapq.heapify(values)

    while len(values) > 1:
        y, x = -heapq.heappop(values), -heapq.heappop(values)

        if x != y:
            z = -(y - x)
            heapq.heappush(values, z)

    if len(values) == 1:
        return -heapq.heappop(values)
    else:
        return 0  