def isPowerOfThree1(num: int) -> bool:
    if num == 1:
        return True

    if num < 1:
        return False

    return isPowerOfThree1(num / 3)

def isPowerOfThree2(num: int) -> bool:
    while num > 1:
        num /= 3

    return num == 1

