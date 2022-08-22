def divisorSubstrings(num: int, k: int) -> int:
    divSub = 0
    numToInt = str(num)
    for i in range(len(numToInt) - k + 1):
        currSub = int(numToInt[i:i+k])
        if currSub != 0 and num % currSub == 0:
            divSub += 1

    return divSub
