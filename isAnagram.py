def isAnagram(s: str, t: str) -> bool:
    element_count1 = {}
    element_count2 = {}
    for i in range(len(s)):
        if s[i] in element_count1:
            element_count1[s[i]] += 1
            continue
        element_count1[s[i]] = 1

    for i in range(len(t)):
        if t[i] in element_count2:
            element_count2[t[i]] += 1
            continue
        element_count2[t[i]] = 1

    if element_count1 == element_count2:
        return True

    return False
