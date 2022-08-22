def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    repeats = {}
    for i in range(len(nums)):
        if nums[i] not in repeats.keys():
            repeats[nums[i]] = i
        else:
            if abs(repeats.get(nums[i]) - i) <= k:
                return True
            else:
                repeats[nums[i]] = i
    return False
