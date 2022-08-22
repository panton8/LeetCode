def majorityElements2(nums: list[int]) -> list[int]:
    repeats = {}
    for i in range(len(nums)):
        if nums[i] not in repeats:
            repeats[nums[i]] = 1
        else:
            repeats[nums[i]] += 1
    majority_list = []
    for key, value in repeats.items():
        if value > len(nums)/3:
            majority_list.append(key)

    return majority_list
