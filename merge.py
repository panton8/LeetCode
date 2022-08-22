def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    index = 0
    for i in range(m, m + n):
        nums1[i] = nums2[index]
        index += 1

    for i in range(len(nums1) - 1):
        for j in range(0, len(nums1) - 1 - i):
            if nums1[j] > nums1[j + 1]:
                nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]
