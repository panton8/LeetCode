def twoSum(nums: list[int], target: int) -> list[int]:
    pos1 = 0
    pos2 = 0
    for i in range(len(nums) - 1):
        for j in range(i, len(nums) - 1):
            if nums[i] + nums[j + 1] == target:
                pos1 = i
                pos2 = j + 1
                break
    return [pos1, pos2]
