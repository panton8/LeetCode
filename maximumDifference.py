def maximumDifference(nums: list[int]) -> int:
    max_increase = -1
    left = 0
    right = 1

    while right < len(nums):
        if nums[left] < nums[right]:
            increase = nums[right] - nums[left]
            max_increase = max(increase, max_increase)
        else:
            left = right
        right += 1

    return max_increase