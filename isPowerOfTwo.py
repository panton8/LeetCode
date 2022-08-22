def isPowerOfTwo(n: int) -> bool:
    while n > 1:
        n /= 2

    return n == 1
