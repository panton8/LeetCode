def reverseString(s, first = 0, last = None):
    if len(s) <= 1:
        return s

    if last == None:
        last = len(s) - 1

    if last < first:
        return s

    tmp = s[first]
    s[first] = s[last]
    s[last] = tmp

    return reverseString(s, first + 1, last - 1)

