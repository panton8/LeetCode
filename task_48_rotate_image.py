def rotate(matrix: list[list[int]]) -> None:
    rotate_matrix = [[0] * len(matrix) for i in range(len(matrix))]
    index = 0
    row = 0
    for i in range(len(matrix)):
        col = 0
        for j in range(len(matrix[i])-1, -1, -1):
            rotate_matrix[row][col] = matrix[j][index]
            col += 1
        index += 1
        row += 1

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = rotate_matrix[i][j]

def main():
    a = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    rotate(a)
    print(a)

if __name__ == "__main__":
    main()