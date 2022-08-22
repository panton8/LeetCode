def minimumOperations(nums: list[int]) -> int:
    while 0 in nums:
        nums.remove(0)
    steps = 0
    while nums:
        min_num = min(nums)
        for i in range(len(nums)):
            nums[i] -= min_num
        while 0 in nums:
            nums.remove(0)
        steps += 1

    return steps
