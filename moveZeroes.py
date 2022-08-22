def moveZeroes(nums: list[int]) -> None :
    index = 0
    zeroes = 0
    notZeroes = 0
    while zeroes + notZeroes != len(nums):
        if nums[index] == 0:
            zeroes += 1
            for j in range(index,len(nums) - 1):
                nums[j] = nums[j+1]
            nums[len(nums) - 1] = 0
        else:
            notZeroes += 1
            index += 1
