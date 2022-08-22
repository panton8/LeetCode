def containsDuplicate(nums: list[int]) -> bool:
    repeats = set()
    for i in range(len(nums)):
        if nums[i] not in repeats:
            repeats.add(nums[i])
        else:
            return True
    return False
