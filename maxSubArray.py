def maxSubArray(nums: list[int]) -> int:
    max_Sub = nums[0]
    cur_Sum = 0

    for num in nums:
        if cur_Sum < 0:
            cur_Sum = 0
        cur_Sum += num
        max_Sub = max(max_Sub, cur_Sum)

    return max_Sub
