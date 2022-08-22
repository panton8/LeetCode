def thirdMax(nums: list[int]) -> int:
    nums = list(set(nums))
    nums.sort()
    nums.reverse()

    if len(nums) < 3:
        return max(nums)

    return nums[2]
