def strStr(haystack: str, needle: str) -> int:
    if not needle or haystack == needle:
        return 0
    return haystack.find(needle)
