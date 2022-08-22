def distributeCandies(candyType: list[int]) -> int:
    types = set(candyType)

    if len(types) >= len(candyType) // 2:
        return len(candyType) // 2
    else:
        return len(types)
