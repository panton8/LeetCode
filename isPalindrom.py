def isPalindrome(s: str) -> bool:
    palindrom = ''
    s = s.lower()
    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <= 'z':
            palindrom += s[i]

    return palindrom == palindrom[::-1]
