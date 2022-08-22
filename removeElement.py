def removeElement(nums: list[int], val: int) -> int:
    not_to_remove = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[not_to_remove] = nums[i]
            not_to_remove += 1
    return not_to_remove

