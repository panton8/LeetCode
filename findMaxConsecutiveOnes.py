def findMaxConsecutiveOnes(nums: list[int]) -> int:
    count = 0
    max_count = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0

    if count > max_count:
        max_count = count

    return max_count
