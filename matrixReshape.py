def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    total_count = 0

    for i in range(len(mat)):
        total_count += len(mat[i])

    if r * c != total_count:
        return mat

    new_mat = [[0] * c for i in range(r)]

    mat_row = len(mat)
    mat_column = total_count / mat_row
    temp_row = 0
    temp_column = 0

    for i in range(r):
        for j in range(c):
            new_mat[i][j] = mat[temp_row][temp_column]
            temp_column += 1
            if temp_column == mat_column:
                temp_column = 0
                temp_row += 1

    return new_mat

