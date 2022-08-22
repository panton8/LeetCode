def longestCommonPrefix(strs: list[str]) -> str:
    if len(strs) == 1:
        return strs[0]
    total_count = 0
    index = 0
    while total_count < len(strs[0]):
        temp_count = 0
        for i in range(1, len(strs)):
            if index < len(strs[i]) and strs[0][index] == strs[i][index]:
                temp_count += 1
        if temp_count == len(strs) - 1:
            total_count += 1
            index += 1
        else:
            return strs[0][:total_count]
    if total_count:
        return strs[0][:total_count]
    return ''

