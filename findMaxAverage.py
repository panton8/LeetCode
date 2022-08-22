def findMaxAverage(nums: list[int], k: int) -> float:
    maxSum = currSum = sum(nums[:k])

    for i in range(k, len(nums)):
        currSum += nums[i] - nums[i-k]
        maxSum = max(currSum, maxSum)

    return maxSum/k
