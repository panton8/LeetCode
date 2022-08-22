def reverseWords(s: str) -> str:
    index = len(s) - 1
    reverse_sent = ''
    word = ''
    space = False

    while index >= 0:
        if s[index] != ' ':
            word += s[index]
            space = True
        if (s[index] == ' ' or index == 0) and space:
            reverse_sent += word[::-1] + ' '
            word = ''
            space = False
        index -= 1

    return reverse_sent[:-1]
