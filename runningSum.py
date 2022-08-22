def runningSum(self, nums: list[int]) -> list[int]:
    self.nums = nums
    sum_nums = [0] * len(nums)
    sum = 0
    for i in range(0, len(nums)):
        sum += nums[i]
        sum_nums[i] = sum
    return sum_nums
