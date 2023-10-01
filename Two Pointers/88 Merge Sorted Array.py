#88. Merge Sorted Array
def merge(nums1, m, nums2, n) -> None:
    r1, r2 = m - 1, n - 1
    while r1 >= 0 and r2 >= 0:
        if nums1[r1] < nums2[r2]:
            nums1[r1 + r2 + 1] = nums2[r2]
            r2 -= 1
        else:
            nums1[r1 + r2 + 1] = nums1[r1]
            r1 -= 1
    if r2 >= 0:
        nums1[:(r2 +1)] = nums2[:(r2 +1)]
