# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guessNumber(self, n: int) -> int:
    first = 1
    last = n
    while first <= last:
        mid = (first + last) // 2
        if guess(mid) == 0:
            return mid
        elif guess(mid) == 1:
            first = mid + 1
        elif guess(mid) == -1:
            last = mid - 1
