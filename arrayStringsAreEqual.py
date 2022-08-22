def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
    str1 = ''
    str2 = ''

    for char in word1:
        str1 += char

    for char in word2:
        str2 += char

    return str2 == str1
