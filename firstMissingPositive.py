def firstMissingPositive(nums: list[int]) -> int:
    positive_list = set()
    for i in range(len(nums)):
        if nums[i] > 0:
            positive_list.add(nums[i])

    min_mis = 1
    for i in range(len(positive_list)):
        if min_mis in positive_list:
            min_mis += 1
        else:
            return min_mis

    return min_mis





def main():
    nums1 = [1, 2, 0]  #3
    nums2 = [3, 4, -1, 1]  #2
    nums3 = [7, 8, 9, 11, 12]  #1
    nums4 = [1,2,5,3,4, 7]

    print(firstMissingPositive(nums1))
    print(firstMissingPositive(nums2))
    print(firstMissingPositive(nums4))

if __name__ == "__main__":
    main()


