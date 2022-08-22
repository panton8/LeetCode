def addDigits(num: int) -> int:
    if num < 10:
        return num
    sum = 0
    while num > 9:
        sum += num % 10
        num //= 10
        if num < 10:
            sum += num
            num = sum
            sum = 0

    return num
