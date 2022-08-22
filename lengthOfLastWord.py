def lengthOfLastWord1(s: str) -> int:
    num_of_words = []
    index = 0

    for i in range(len(s)):
        if s[i] == ' ':
            if i > 0 and (s[i] == ' ' and s[i - 1] != ' '):
                index += 1
            continue
        else:
            if i == 0 or s[i - 1] == ' ':
                num_of_words.append('')
            num_of_words[index] += s[i]

    return len(num_of_words[-1])

def lengthOfLastWord2(s: str) -> int:
    lastLen = 0

    for i in range(len(s)):
        if s[i] != ' ':
            if i > 0 and s[i - 1] == ' ':
                lastLen = 0
            lastLen += 1

    return lastLen
