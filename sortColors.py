def sortColors(nums: list[int]) -> None:
    for i in range(len(nums) - 1):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
