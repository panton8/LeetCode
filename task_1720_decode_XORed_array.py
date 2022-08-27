def decode(encoded: list[int], first: int) -> list[int]:
    prev_arr = [first]
    for i in range(len(encoded)):
        prev_arr.append(encoded[i] ^ prev_arr[i])

    return prev_arr


def main():
    print(decode([6, 2, 7, 3], 4))
    print(decode([6], 1))


if __name__ == "__main__":
    main()
