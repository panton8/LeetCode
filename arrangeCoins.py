def arrangeCoins(n: int) -> int:
    row_value = 1

    while True:
        n -= row_value
        if n < row_value + 1:
            return row_value
        row_value += 1
