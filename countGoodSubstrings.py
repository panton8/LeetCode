def countGoodSubstrings(s: str):
    subCount = 0
    for i in range(len(s) - 3 + 1):
        currSub = s[i:i + 3]
        if len(set(currSub)) == len(currSub):
            subCount += 1

    return subCount
