def maximumWealth(accounts: list[list[int]]) -> int:
    sum = [0] * len(accounts)
    for i in range(len(accounts)):
        for j in range(len(accounts[i])):
            sum[i] += accounts[i][j]

    sum.sort()
    return sum[len(sum) - 1]
