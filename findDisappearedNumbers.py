def findDisappearedNumbers(nums: list[int]) -> list[int]:
    disappeared_nums = []
    nums_set = set()
    nums.sort()
    for i in range(len(nums)):
        if nums[i] not in nums_set:
            nums_set.add(nums[i])
        else:
            nums[i] = float('inf')
    nums.sort()

    for i in range(len(nums)):
        if nums[i] != i + 1:
            disappeared_nums.append(i+1)
            nums.insert(i, i+1)

    return disappeared_nums
