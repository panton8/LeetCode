def minimumAbsDifference(arr: list[int]) -> list[list[int]]:
    arr.sort()
    dif_arr = []

    for i in range(len(arr) - 1, 0, -1):
        dif_arr.append(arr[i] - arr[i - 1])

    abs_min = []
    min_dif = min(dif_arr)

    for i in range(1, len(dif_arr) + 1):
        if arr[i] - arr[i - 1] == min_dif:
            temp = [arr[i - 1], arr[i]]
            abs_min.append(temp)

    return abs_min


def main():
    print(minimumAbsDifference([4, 2, 3, 1]))

    assert minimumAbsDifference([40, 11, 26, 27, -20]) == [[26, 27]]


if __name__ == "__main__":
    main()
