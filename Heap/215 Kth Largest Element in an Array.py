import heapq

def findKthLargest(nums, k):
    
    values = [-x for x in nums]
    heapq.heapify(values)

    for _ in range(k):
        x = heapq.heappop(values)
    
    return -x