def majorityElement(nums: list[int]) -> int:
    repeats = {}
    for i in range(len(nums)):
        if nums[i] not in repeats:
            repeats[nums[i]] = 1
        else:
            repeats[nums[i]] += 1
    max_repeat = max(repeats.values())
    for key,value in repeats.items():
        if value == max_repeat:
            return key
