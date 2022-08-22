def findNumbers(nums: list[int]) -> int:
    total_even_digit = 0
    for i in nums:
        temp_even_digit = 1
        while i >= 10:
            i /= 10
            temp_even_digit += 1
        if temp_even_digit % 2 == 0:
            total_even_digit += 1

    return total_even_digit
