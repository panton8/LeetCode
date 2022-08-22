def mostWordsFound(sentences: list[str]) -> int:
    word_count = []

    for i in range(len(sentences)):
        word_num = 1
        for j in range(len(sentences[i])):
            if sentences[i][j] != ' ' and sentences[i][j-1] == ' ':
                word_num += 1
        word_count.append(word_num)

    return max(word_count)
