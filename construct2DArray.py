def construct2DArray(original: list[int], m: int, n: int) -> list[list[int]]:
    if m * n != len(original):
        return []

    _2D_Array = [[0] * n for i in range(m)]
    index = 0

    for i in range(m):
        for j in range(n):
            _2D_Array[i][j] = original[index]
            index += 1

    return _2D_Array
