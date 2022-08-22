def duplicateZeros(arr: list[int]) -> None:
    flag = -1
    for i in range(len(arr)):
        if arr[i] == 0 and i != len(arr) - 1 and i != flag:
            for j in range(len(arr) - 1, i + 1, -1):
                arr[j] = arr[j - 1]
            arr[i + 1] = 0
            flag = i + 1
