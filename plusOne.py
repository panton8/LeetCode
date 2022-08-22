def plusOne(digits: list[int]) -> list[int]:
    if digits[len(digits) - 1] != 9:
        digits[len(digits) - 1] += 1
        return digits

    index = 1
    while index <= len(digits) and digits[len(digits) - index] == 9:
        digits[len(digits) - index] = 0
        index += 1
    if (digits[0] == 9 or digits[0] == 0) and len(digits) == index:
        digits.insert(0, 1)
    else:
        if len(digits) < index:
            digits.insert(0, 1)
        else:
            digits[len(digits) - index] += 1
    return digits
