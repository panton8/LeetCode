def searchInsert(nums: list[int], target: int) -> int:
    first_index = 0
    last_index = len(nums)-1

    while first_index <= last_index:
        mid = (first_index + last_index) // 2

        if target == nums[mid]:
            return mid

        elif target > nums[mid]:
            if mid + 1 > last_index:
                return mid + 1
            first_index = mid + 1

        elif target < nums[mid]:
            if mid - 1 < first_index:
                return mid
            last_index = mid - 1