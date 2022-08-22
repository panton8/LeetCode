def reverse(x: int) -> int:
    copy = abs(x)
    digit_count = 0

    while copy >= 1:
        digit_count += 1
        copy //= 10

    if not digit_count:
        digit_count += 1

    new_num = 0
    sign = 1
    if x >= 0:
        sign = 1
    else:
        sign = -1

    x = abs(x)
    while x >= 1:
        new_num += (x % 10) * (10 ** (digit_count - 1))
        x //= 10
        digit_count -= 1

    new_num *= sign

    if new_num < -2 ** 31 or new_num > 2 ** 31 - 1:
        return 0
    return new_num
