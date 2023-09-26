#347. Top K Frequent Elements

def create_frec_hashmap(nums):
    res = {}

    for n in nums:
        if n in res:
            res[n] += 1
        else:
            res[n] = 1
    
    return res

def create_frec_array(nums, num_count):
    res = [[] for n in range((len(nums) + 1))]
    
    for k, v in num_count.items():
        res[v].append(k)
    
    return res

def topKFrequent(nums, k):

    aux = create_frec_array(nums, create_frec_hashmap(nums))
    res = []
    for i in range(len(aux)-1, -1, -1):
        if aux[i] != []:
            res.extend(aux[i])
        if len(res) >= k:
            return res
    return res

topKFrequent([1,1,1,2,2,3], 2)