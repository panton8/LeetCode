def findMin1(nums: List[int]) -> int:
    min_num = nums[0]

    for num in nums:
        if num < min_num:
            min_num = num

    return min_num


def findMin2(nums: List[int]) -> int:
    return min(nums)