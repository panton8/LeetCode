def lastStoneWeight(stones: list[int]) -> int:
    stones.sort()

    while len(stones) > 1:
        st1, st2 = stones[-1], stones[-2]

        stones.remove(stones[-1])
        stones.remove(stones[-1])

        if st1 - st2 > 0:
            stones.append(st1 - st2)

        stones.sort()

    if stones:
        return stones[0]
    return 0

def main():
    print(lastStoneWeight([2, 7, 4, 1, 8, 1]))

if __name__ == "__main__":
    main()
