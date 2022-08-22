def missingNumber1(nums: list[int]) -> int:
    num_kind = set()

    for i in range(len(nums)):
        num_kind.add(nums[i])

    for i in range(len(nums)+1):
        if i not in num_kind:
            return i


def missingNumber2(nums: list[int]) -> int:
    total_sum = 0

    count = len(nums)

    while count:
        total_sum += count
        count -= 1

    for num in nums:
        total_sum -= num

    return total_sum
