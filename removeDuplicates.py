def removeDuplicates(nums: list[int]) -> int:
    index = 0
    for i in range(len(nums)):
        if i + 1 < len(nums) and nums[i] != nums[i + 1]:
            nums[index] = nums[i]
            index += 1
        elif i + 1 == len(nums):
            nums[index] = nums[i]
            index += 1

    return index