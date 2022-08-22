def isPalindrome(x: int):
    num1 = str(x)
    num2 = num1[::-1]

    if num1 == num2:
        return True

    return False
