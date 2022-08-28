def decodeMessage(key: str, message: str) -> str:
    table = []

    for char in key:
        if char not in table and char != ' ':
            table.append(char)

    rel = {}
    code = 97

    for char in table:
        rel[char] = chr(code)
        code += 1

    dec_message = ''

    for char in message:
        if char != ' ':
            dec_message += rel[char]
            continue
        dec_message += ' '

    return dec_message


def main():
    print(decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))

    assert decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv") == "this is a secret"


if __name__ == "__main__":
    main()
