def toLowerCase1(s: str) -> str:
    return s.lower()


def toLowerCase2(s: str) -> str:
    for i in range(len(s)):
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            s = s[:i] + chr(ord(s[i]) + 32) + s[i+1:]

    return s


def main():
    print(toLowerCase1('Hello'))

    assert toLowerCase2('LoVeLy') == 'lovely'


if __name__ == '__main__':
    main()
