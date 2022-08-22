def findDuplicate(self, nums: List[int]) -> int:
    numbers_count = {}

    for i in range(len(nums)):
        if nums[i] not in numbers_count.keys():
            numbers_count[nums[i]] = 1
        else:
            numbers_count[nums[i]] += 1

    for key, value in numbers_count.items():
        if value >= 2:
            return key
