def commonChars(words: list[str]) -> list[str]:
    common_list = []
    all_words = True

    for i in range(len(words[0])):
        for j in range(1, len(words)):
            if words[0][i] not in words[j]:
                all_words = False
                break
        if all_words:
            common_list.append(words[0][i])
            for j in range(1, len(words)):
                words[j] = words[j].replace(words[0][i], ' ')
        all_words = True

    return common_list
