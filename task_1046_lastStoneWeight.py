def lastStoneWeight(stones: list[int]) -> int:
    while len(stones) > 1:
        st1 = max(stones)
        stones.remove(max(stones))
        st2 = max(stones)
        stones.remove(max(stones))

        if st1 - st2 > 0:
            stones.append(st1 - st2)

    if stones:
        return stones[0]
    return 0


def main():
    print(lastStoneWeight([2, 7, 4, 1, 8, 1]))

    assert lastStoneWeight([1]) == 1


if __name__ == "__main__":
    main()
