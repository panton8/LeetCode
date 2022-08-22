def lengthOfLongestSubstring(s: str) -> int:
    myset = {}
    temp_res = 0
    max_res = 0
    i = 0
    while i < len(s):
        if s[i] not in myset.keys():
            myset[s[i]] = i
            temp_res += 1
        else:
            new_start = myset[s[i]]
            myset.clear()
            if temp_res > max_res:
                max_res = temp_res
            temp_res = 0
            i = new_start
        i += 1

    if temp_res > max_res:
        return temp_res
    return max_res
