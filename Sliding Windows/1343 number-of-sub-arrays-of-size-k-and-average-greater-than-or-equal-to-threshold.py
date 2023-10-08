#1343 number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-thresho

def numOfSubarrays(arr, k, threshold):
    ans = 0
    cumSum = sum(arr[:k-1])

    for L in range(len(arr) - k + 1):
        cumSum += arr[L + k - 1]
        if (cumSum / k) >= threshold:
            ans += 1
        cumSum -= arr[L]
    return ans

numOfSubarrays([2,2,2,2,5,5,5,8],3,4)