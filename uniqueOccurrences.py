def uniqueOccurrences(arr: list[int]) -> bool:
    total_oc = {}

    for num in arr:
        if num in total_oc:
            total_oc[num] += 1
        else:
            total_oc[num] = 1

    list1 = list(total_oc.values())
    list2 = set(total_oc.values())

    return len(list1) == len(list2)
