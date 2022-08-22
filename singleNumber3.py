def singleNumber(nums: List[int]) -> List[int]:
    numbers_count = {}

    for i in range(len(nums)):
        if nums[i] not in numbers_count.keys():
            numbers_count[nums[i]] = 1
        else:
            numbers_count[nums[i]] += 1

    single_num_list = []

    for key, value in numbers_count.items():
        if value == 1:
            single_num_list.append(key)

    return single_num_list
